# from application.ninja_cof import api
# Author 臧成龙
# coding=utf-8
# @Time    : 2022/5/29 01:36
# @File    : user.py
# @Software: PyCharm
# @qq: 939589097

from typing import List

from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Schema, Field
from ninja.pagination import paginate
from system.models import Users
from utils.fu_crud import create, delete, retrieve

from utils.fu_ninga import MyPagination, FuFilters
from utils.fu_response import FuResponse

router = Router()


class Filters(FuFilters):
    name: str = Field(None, alias="name")
    mobile: str = Field(None, alias="mobile")
    status: bool = Field(None, alias="status")
    id: int = Field(None, alias="id")


class SchemaIn(ModelSchema):
    dept_id: int = Field(None, alias="dept")
    post: list = []
    role: list = []

    class Config:
        model = Users
        model_exclude = ['id', 'groups', 'user_permissions', 'is_superuser', 'dept', 'post', 'role', 'password',
                         'create_datetime', 'update_datetime']


class SchemaOut(ModelSchema):
    class Config:
        model = Users
        model_exclude = ['password']


@router.post("/user", response=SchemaOut)
def create_user(request, data: SchemaIn):
    data_dic = data.dict()
    data_dic['password'] = make_password('123456')
    post = data_dic.pop('post')
    role = data_dic.pop('role')
    user = create(request, data_dic, Users)
    # 为多对多关系添加数据
    user.post.set(post)
    user.role.set(role)
    return user


@router.delete("/user/{user_id}")
def delete_user(request, user_id: int):
    delete(user_id, Users)
    return {"success": True}


@router.put("/user/{user_id}", response=SchemaOut)
def update_user(request, user_id: int, payload: SchemaIn):
    user = get_object_or_404(Users, id=user_id)
    for attr, value in payload.dict().items():
        if attr == 'role':
            user.role.set(value)
        elif attr == 'post':
            user.post.set(value)
        else:
            setattr(user, attr, value)
    user.save()
    return user


@router.get("/user", response=List[SchemaOut])
@paginate(MyPagination)
def list_user(request, filters: Filters = Query(...)):
    qs = retrieve(request, Users, filters)
    return qs


@router.get("/user/all/list", response=List[SchemaOut])
def all_list_user(request):
    qs = retrieve(request, Users)
    return qs


@router.get("/user/{user_id}", response=SchemaOut)
def get_user(request, user_id: int):
    user = get_object_or_404(Users, id=user_id)
    return user


class SchemaIn(Schema):
    id: int
    password: str
    old_password: str
    verify_password: str

@router.post("/user/set/repassword", response=SchemaOut)
def repassword(request, data: SchemaIn):
    user = get_object_or_404(Users, id=data.id)
    old_pwd = data.old_password
    new_pwd = data.password
    new_pwd2 = data.verify_password
    if user:
        if new_pwd != new_pwd2:
            return FuResponse(msg="两次密码不匹配")
        elif user.check_password(old_pwd):
            user.password = make_password(new_pwd)
            user.save()
            return FuResponse(msg="修改成功")
        else:
            return FuResponse(code=1, msg="旧密码不正确")

    else:
        return FuResponse(code=1, msg="未获取到用户")
    return FuResponse(msg='密码重置成功')
