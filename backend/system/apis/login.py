# -*- coding: utf-8 -*-
# @Time    : 2022/5/14 15:05
# @Author  : 臧成龙
# @FileName: login.py
# @Software: PyCharm
import json
from datetime import datetime, timedelta

from django.contrib.auth.hashers import check_password
from django.core.cache import cache

from django.contrib import auth
from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Schema, Field

from fuadmin.settings import SECRET_KEY, TOKEN_LIFETIME
from system.models import Users, Role, MenuButton, CaptchaStore
from utils.fu_jwt import FuJwt
from utils.fu_response import FuResponse
from utils.request_util import save_login_log
from utils.usual import get_user_info_from_token

router = Router()


class SchemaOut(ModelSchema):

    class Config:
        model = Users
        model_exclude = ['password', 'role', 'post']


class LoginSchema(Schema):
    username: str = Field(None, alias="username")
    password: str = Field(None, alias="password")
    captcha: str = Field(None, alias="captcha")
    captch_id: str = Field(None, alias="captch_id")


class Out(Schema):
    multi_depart: str
    sysAllDictItems: str
    departs: str
    userInfo: SchemaOut
    token: str


@router.post("/login", response=Out, auth=None)
def login(request, data: LoginSchema):
    username = data.username
    password = data.password
    captch_id = data.captch_id
    captcha = data.captcha
    if captch_id is None:
        return FuResponse(code=500, msg="验证码不能为空")
    image_code = CaptchaStore.objects.get(id=captch_id)
    five_minute_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
    if image_code and five_minute_ago > image_code.expiration:
        image_code and image_code.delete()
        return FuResponse(code=500, msg="验证码过期")
    else:
        if image_code and (image_code.response == captcha.lower()):
            image_code and image_code.delete()
        else:
            image_code and image_code.delete()
            return FuResponse(code=500, msg="图片验证码错误")
    user = Users.objects.filter(username=username, is_active=True, password__isnull=False).first()
    if (datetime.now() - user.login_suo).total_seconds() < 3000:
        return FuResponse(code=500, msg="账号锁定三十分钟内不能登陆！")
    else:
        user.pass_errnum = 0
    if user.pass_errnum > 5:
        user.login_suo = datetime.now()
        return FuResponse(code=500, msg="密码输入超过5次，用户锁定三十分钟！")
    if check_password(password, user.password):
        request.user = user
        role = user.role.all().values('id')
        post = list(user.post.all().values('id'))
        role_list = []
        post_list = []
        for item in role:
            role_list.append(item['id'])
        for item in post:
            post_list.append(item['id'])
        user_obj_dic = model_to_dict(user)
        user_obj_dic['post'] = post_list
        user_obj_dic['role'] = role_list
        del user_obj_dic['password']
        del user_obj_dic['avatar']

        time_now = int(datetime.now().timestamp())
        jwt = FuJwt(SECRET_KEY, user_obj_dic, valid_to=time_now + TOKEN_LIFETIME)
        # 将生成的token加入缓存
        cache.set(user.id, jwt.encode())
        token = f"bearer {jwt.encode()}"
        data = {
            "multi_depart": 1,
            "sysAllDictItems": "q",
            "departs": "e",
            'userInfo': user_obj_dic,
            'token': token
        }
        save_login_log(request=request)
        return data
    else:
        user.pass_errnum += 1
        user.save()
        return FuResponse(code=500, msg="账号/密码不正确！")


@router.get("/logout", auth=None)
def get_post(request):
    # 删除缓存
    user_info = get_user_info_from_token(request)
    cache.delete(user_info['id'])
    return FuResponse(msg="注销成功")


@router.get("/userinfo", response=SchemaOut)
def get_userinfo(request):
    user_info = get_user_info_from_token(request)
    user = get_object_or_404(Users, id=user_info['id'])
    return user


@router.get("/permCode")
def route_menu_tree(request):
    """用于前端获取当前用户的按钮权限"""
    token_user = get_user_info_from_token(request)
    user = Users.objects.get(id=token_user['id'])
    queryset = MenuButton.objects.all()
    if not token_user['is_superuser']:
        menuIds = user.role.values_list('permission__id', flat=True)
        # queryset = MenuButton.objects.filter(id__in=menuIds, status=1).values()
        queryset = MenuButton.objects.filter(id__in=menuIds)
    code_list = []
    for item in queryset:
        code_list.append(item.code)
    return FuResponse(data=code_list)
