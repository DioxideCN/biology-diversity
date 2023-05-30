
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Field
from ninja.pagination import paginate

from biology.models import Areas
from utils.fu_crud import delete, update, retrieve, ImportSchema, export_data, import_data
from utils.fu_ninga import MyPagination, FuFilters

from django.utils import timezone
from utils.usual import get_user_info_from_token
import random

import json

router = Router()


def create(request, data, model):
    if not isinstance(data, dict):
        data = data.dict()
    user_info = get_user_info_from_token(request)
    # 创建时默认添加创建人、修改者和所属部门
    data['creator_id'] = user_info['id']
    data['modifier'] = user_info['name']
    data['belong_dept'] = user_info['dept']
    random_number = random.randint(1, 9999)
    date = timezone.now().strftime("%Y%m%d")
    if random_number < 10:
        data['id'] = 'DV' + date + '000' + str(random_number)
    elif random_number < 100:
        data['id'] = 'DV' + date + '00' + str(random_number)
    elif random_number < 1000:
        data['id'] = 'DV' + date + '0' + str(random_number)
    else:
        data['id'] = 'DV' + date + str(random_number)
    query_set = model.objects.create(**data)
    return query_set

# 设置过滤字段 提前将字段转型
class Filters(FuFilters):
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    address: str = Field(None, alias="address")
    manager: str = Field(None, alias="manager")
    type: str = Field(None, alias="type")


# 设置请求接收字段
class AreasManageSchemaIn(ModelSchema):
    class Config:
        model = Areas
        model_fields = ['name', 'address', 'manager', 'manager_phone', 'introduction', 'notes', 'path', 'type']


# 设置响应字段
class AreasManageSchemaOut(ModelSchema):
    class Config:
        model = Areas
        model_fields = "__all__"


# 创建Areas
@router.post("/area_manage", response=AreasManageSchemaOut)
def create_area(request, data: AreasManageSchemaIn):
    # 调用封装的create函数
    area = create(request, data, Areas)
    return area


# 删除Areas
@router.delete("/area_manage/{area_id}")
def delete_area(request, area_id: str):
    delete(area_id, Areas)
    return {"success": True}


# 更新Areas
@router.put("/area_manage/{area_id}", response=AreasManageSchemaOut)
def update_area(request, area_id: str, data: AreasManageSchemaIn):
    area = update(request, area_id, data, Areas)
    return area


# 获取Areas 并分页
@router.get("/area_manage", response=List[AreasManageSchemaOut])
@paginate(MyPagination)
def list_area(request, filters: Filters = Query(...)):
    qs = retrieve(request, Areas, filters)
    return qs


# 获取Areas的name和id 并分页
@router.get("/area/manage", response=List[AreasManageSchemaOut])
@paginate(MyPagination)
def list_area(request):
    qs = Areas.objects.all().values_list('id', 'name')
    return qs


# 获取所有区域
@router.get("/area_manage/all/list")
def all_list_area(request):
    qs = retrieve(request, Areas)
    areas = []
    for unit in qs:
        data = {}
        data['path'] = json.loads(unit.path)
        data['id'] = unit.id
        data['name'] = unit.name
        data['address'] = unit.address
        data['manager'] = unit.manager
        data['manager_phone'] = unit.manager_phone
        data['introduction'] = unit.introduction
        data['notes'] = unit.notes
        data['type'] = unit.type
        areas.append(data)
    return {
        "success": True,
        "result": areas,
        "code": 200,
        "message": "success"
    }


# 根据id获取单个动物
@router.get("/area_manage/{area_id}")
def get_area(request, area_id: str):
    area = get_object_or_404(Areas, id=area_id)
    area.path = json.loads(area.path)
    data = {}
    data['path'] = area.path
    data['id'] = area.id
    data['name'] = area.name
    data['address'] = area.address
    data['manager'] = area.manager
    data['manager_phone'] = area.manager_phone
    data['introduction'] = area.introduction
    data['notes'] = area.notes
    data['type'] = area.type
    return {
        "success": True,
        "result": data,
        "code": 200,
        "message": "success"
    }


# # 导入
# @router.get("/area/all/export")
# def export_area(request):
#     title_dict = {
#         'name': '名称',
#         'code': '编码',
#         'status': '状态',
#         'sort': '排序',
#     }
#     return export_data(request, Areas, AreasManageSchemaOut, title_dict)
#
#
# # 导出
# @router.post("/area/all/import")
# def import_area(request, data: ImportSchema):
#     title_dict = {
#         '名称': 'name',
#         '编码': 'code',
#         '状态': 'status',
#         '排序': 'sort',
#     }
#     return import_data(request, Areas, AreasManageSchemaIn, data, title_dict)
