import base64
import json
from dataclasses import Field

from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from captcha.views import captcha_image
from django.http import HttpResponse, JsonResponse
from ninja import Router, ModelSchema, Schema, Field

from utils.fu_ninga import FuFilters
from system.models import CaptchaStore
from utils.capt_util import captcha_image
from utils.fu_ninga import FuFilters

router = Router()


# 设置过滤字段 提前将字段转型
class Filters(FuFilters):
    challenge: str = Field(None, alias="challenge")
    response: str = Field(None, alias="response")
    hashkey: str = Field(None, alias="hashkey")
    expiration: str = Field(None, alias="expiration")


# 设置请求接收字段
class CaptchaSchemaIn(ModelSchema):
    class Config:
        model = CaptchaStore
        model_fields = "__all__"


# 设置响应字段
class CaptchaSchemaOut(ModelSchema):
    class Config:
        model = CaptchaStore
        model_fields = "__all__"


# 创建验证码
def create_captcha():
    hashkey = CaptchaStore.generate_key()  # 验证码答案
    image_url = captcha_image_url(hashkey)  # 验证码地址
    captcha = {'hashkey': hashkey, 'image_url': image_url}
    return captcha


# 刷新验证码
# 接口未被调用，前端直接再次调用生成验证码接口，刷新验证码
@router.get("/refreshCaptcha")
def refresh_captcha(request):
    return JsonResponse(create_captcha())


# 验证函数
def jarge_captcha(captchaStr, captchaHashkey):
    # get_captcha = CaptchaStore.objects.get(hashkey=captchaHashkey)
    # if get_captcha.response == captchaStr.lower():
    #     return True
    # else:
    #     return False
    # print("str: " + captchaStr + " key: " + captchaHashkey)
    if captchaStr and captchaHashkey:
        try:
            # 获取根据hashkey获取数据库中的response值
            get_captcha = CaptchaStore.objects.get(hashkey=captchaHashkey)
            if get_captcha.response == captchaStr.lower():  # 如果验证码匹配
                return True
        except:
            return False
    else:
        return False


# 生成验证码
@router.get("/getCode", response=CaptchaSchemaOut, auth=None)
def get_code(request):
    hashkey = CaptchaStore.generate_key()  # 验证码答案
    id = CaptchaStore.objects.filter(hashkey=hashkey).first().id
    image = captcha_image(request, id)
    image_url = 'data:image/png;base64,%s' % base64.b64encode(image.content).decode('utf-8')
    # 定期删除过期验证码
    CaptchaStore.remove_expired()
    captcha = {'captch_id': id, 'image_url': image_url, 'code': 200}
    return JsonResponse(captcha)
    # return HttpResponse(json.dumps(captcha), content_type='application/json')


# 核对验证码
# @router.post("/postCode", auth=None)
# def post(request):
#     data = json.loads(request.body)
#     capt = data['response'] # 用户提交的验证码
#     key = data['hashkey']  # 验证码答案
#     response = {'code': -1, 'message': ''}
#     if jarge_captcha(capt, key):
#         response['code'] = 200
#         response['message'] = "验证成功"
#         return JsonResponse(response)
#     else:
#         response['code'] = -1
#         response['message'] = "验证失败"
#         return JsonResponse(response)