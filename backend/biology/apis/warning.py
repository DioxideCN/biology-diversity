
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Field
from ninja.pagination import paginate

from biology.models import Warning
from utils.fu_crud import create, delete, update, retrieve, ImportSchema, export_data, import_data
from utils.fu_ninga import MyPagination, FuFilters

router = Router()


# 设置过滤字段 提前将字段转型
class Filters(FuFilters):
    id: int = Field(None, alias="id")
    type: str = Field(None, alias="type")
    message: str = Field(None, alias="message")


# 设置请求接收字段
class WarningSchemaIn(ModelSchema):
    class Config:
        model = Warning
        model_fields = ['type', 'message']


# 设置响应字段
class WarningSchemaOut(ModelSchema):
    class Config:
        model = Warning
        model_fields = "__all__"


# 创建Warning
@router.post("/warning", response=WarningSchemaOut)
def create_warning(request, data: WarningSchemaIn):
    # 调用封装的create函数
    warning = create(request, data, Warning)
    return warning


# 删除Warning
@router.delete("/warning/{warning_id}")
def delete_warning(request, warning_id: int):
    delete(warning_id, Warning)
    return {"success": True}


# 更新Warning
@router.put("/warning/{warning_id}", response=WarningSchemaOut)
def update_warning(request, warning_id: int, data: WarningSchemaIn):
    warning = update(request, warning_id, data, Warning)
    return warning


# 获取Warning 并分页
@router.get("/warning", response=List[WarningSchemaOut])
@paginate(MyPagination)
def list_warning(request, filters: Filters = Query(...)):
    qs = retrieve(request, Warning, filters)
    return qs


# 获取所有预警信息
@router.get("/warning/all/list", response=List[WarningSchemaOut])
def all_list_warning(request):
    qs = retrieve(request, Warning)
    return qs


# 根据id获取单个预警信息
@router.get("/warning/{warning_id}", response=WarningSchemaOut)
def get_warning(request, warning_id: int):
    warning = get_object_or_404(Warning, id=warning_id)
    return warning


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
