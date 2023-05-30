
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Field
from ninja.pagination import paginate

from biology.models import Botany_classification
from utils.fu_crud import create, delete, update, retrieve, ImportSchema, export_data, import_data
from utils.fu_ninga import MyPagination, FuFilters

router = Router()


# 设置过滤字段 提前将字段转型
class Filters(FuFilters):
    id: int = Field(None, alias="id")
    name: str = Field(None, alias="name")
    botany_id: str = Field(None, alias="botany_id")
    type: str = Field(None, alias="type")

# 设置请求接收字段
class BotanySchemaIn(ModelSchema):
    class Config:
        model = Botany_classification
        model_fields = ['name', 'notes', 'type', 'botany_id']


# 设置响应字段
class BotanySchemaOut(ModelSchema):
    class Config:
        model = Botany_classification
        model_fields = "__all__"


# 创建Botany
@router.post("/botany_classification", response=BotanySchemaOut)
def create_botany(request, data: BotanySchemaIn):
    # 调用封装的create函数
    botany = create(request, data, Botany_classification)
    return botany


# 删除Botany
@router.delete("/botany_classification/{botany_id}")
def delete_botany(request, botany_id: int):
    delete(botany_id, Botany_classification)
    return {"success": True}


# 更新Botany
@router.put("/botany_classification/{botany_id}", response=BotanySchemaOut)
def update_botany(request, botany_id: int, data: BotanySchemaIn):
    botany = update(request, botany_id, data, Botany_classification)
    return botany


# 获取Botany 并分页
@router.get("/botany_classification", response=List[BotanySchemaOut])
@paginate(MyPagination)
def list_botany(request, filters: Filters = Query(...)):
    qs = retrieve(request, Botany_classification, filters)
    return qs


# 获取所有植物
@router.get("/botany_classification/all/list", response=List[BotanySchemaOut])
def all_list_botany(request):
    qs = retrieve(request, Botany_classification)
    return qs


# 根据id获取单个植物
@router.get("/botany_classification/{botany_id}", response=BotanySchemaOut)
def get_botany(request, botany_id: int):
    botany = get_object_or_404(Botany_classification, id=botany_id)
    return botany


# # 导入
# @router.get("/animal/all/export")
# def export_animal(request):
#     title_dict = {
#         'name': '名称',
#         'code': '编码',
#         'status': '状态',
#         'sort': '排序',
#     }
#     return export_data(request, Animal, AnimalSchemaOut, title_dict)
#
#
# # 导出
# @router.post("/animal/all/import")
# def import_animal(request, data: ImportSchema):
#     title_dict = {
#         '名称': 'name',
#         '编码': 'code',
#         '状态': 'status',
#         '排序': 'sort',
#     }
#     return import_data(request, Animal, AnimalSchemaIn, data, title_dict)
