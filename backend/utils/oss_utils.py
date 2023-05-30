import os
import uuid
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import oss2
from fuadmin.settings import *

# 用户账号密码，第三部说明的Access
# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
# 获取的AccessKey
auth = oss2.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
# 这个是需要用特定的地址，不同地域的服务器地址不同，不要弄错了
endpoint = EndPoint
# 你的项目名称，类似于不同的项目上传的文件前缀url不同
# 因为我用的是ajax传到后端方法接受的是b字节文件，需要如下配置。 阿里云oss支持更多的方式，下面有链接可以自己根据自己的需求去写
bucket = oss2.Bucket(auth, endpoint, ProjectName)  # 项目名称

# 这个是上传文件后阿里云返回的uri需要拼接下面这个url才可以访问，根据自己情况去写这步
base_file_url = Base_File_URL


# Create your views here.
def index(request):
    return render(request,'index.html')

# 进度条
# 当无法确定待上传的数据长度时，total_bytes的值为None。
def percentage(consumed_bytes, total_bytes):
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print('\r{0}% '.format(rate), end='')


def update_fil_file(file):
    """
    ！ 上传文件
    :param file: b字节文件
    :return: 若成功返回文件路径，若不成功返回空
    """
    # 生成文件编号，如果文件名重复的话在oss中会覆盖之前的文件
    current_date = datetime.now().strftime('%Y%m%d%H%M%S%f')
    file_name = current_date + '_' + file.name.replace(' ', '_')
    # 生成文件名
    base_fil_name = file_name
    # 生成外网访问的文件路径
    file_name = base_file_url + base_fil_name
    # 这个是阿里提供的SDK方法 bucket是调用的4.1中配置的变量名
    res = bucket.put_object(base_fil_name, file, progress_callback=percentage)
    # 如果上传状态是200 代表成功 返回文件外网访问路径
    # 下面代码根据自己的需求写
    if res.status == 200:
        return file_name
    else:
        return False

@csrf_exempt
def test(request):
    if request.method == 'POST':
        # 获取前端ajax传的文件 使用read()读取b字节文件
        file = request.FILES.get('file').read()
        # 通过上面封装的方法把文件上传
        file_url = update_fil_file(file)
        print(file_url)
        # 这里没有做判断验证只是测试代码 根据自己的需求需要判断
        return HttpResponse('上传成功')
