from typing import List

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Field
from ninja.pagination import paginate

from biology.models import Title
from utils.fu_crud import create, delete, update, retrieve, ImportSchema, export_data, import_data
from utils.fu_ninga import MyPagination, FuFilters

router = Router()


# 设置过滤字段 提前将字段转型
class Filters(FuFilters):
    name: str = Field(None, alias="name")


# 设置请求接收字段
class TitleSchemaIn(ModelSchema):
    class Config:
        model = Title
        model_fields = ['name']


# 设置响应字段

class TitleSchemaOut(ModelSchema):
    class Config:
        model = Title
        model_fields = "__all__"


# 更新Title
@router.put("/title")
def update_title(request, data: TitleSchemaIn):
    instance = Title.objects.all().first()
    # instance = init_title[0]
    instance.name = data.name
    name = data.name
    instance.save()
    # id = 1
    data = {
        'name': name,
        'id': 1,
    }
    return data


@router.get("/title")
def get_title(request):
    # title = get_object_or_404(Title, title_id=title_id)
    title = Title.objects.all().first()
    data = {
        'name': title.name,
        'id': title.id
    }
    return data

# # 导入
# @router.get("/title/all/export")
# def export_title(request):
#     title_dict = {
#         'name': '名称',
#         'code': '编码',
#         'status': '状态',
#         'sort': '排序',
#     }
#     return export_data(request, Title, TitleSchemaOut, title_dict)
#
#
# # 导出
# @router.post("/title/all/import")
# def import_title(request, data: ImportSchema):
#     title_dict = {
#         '名称': 'name',
#         '编码': 'code',
#         '状态': 'status',
#         '排序': 'sort',
#     }
#     return import_data(request, Title, TitleSchemaIn, data, title_dict)
