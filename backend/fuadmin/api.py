# -*- coding: utf-8 -*-
# @Time    : 2022/5/9 23:15
# @Author  : 臧成龙
# @FileName: api.py
# @Software: PyCharm
from biology.router import biology_router
from system.router import system_router
from utils.fu_auth import GlobalAuth
from utils.fu_ninga import FuNinjaAPI

api = FuNinjaAPI(auth=GlobalAuth())


# 统一处理server异常
@api.exception_handler(Exception)
def a(request, exc):

    if hasattr(exc, 'errno'):
        return api.create_response(request, data=[], msg=str(exc), code=exc.errno)
    else:
        return api.create_response(request, data=[], msg=str(exc), code=500)


api.add_router('/system/', system_router)
api.add_router('/biology/', biology_router)
