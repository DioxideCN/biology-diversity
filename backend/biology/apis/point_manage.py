import json
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Field
from ninja.pagination import paginate

from biology.models import Point
from utils.fu_crud import delete, update, retrieve, ImportSchema, export_data, import_data
from utils.fu_ninga import MyPagination, FuFilters

from django.utils import timezone

from utils.fu_response import FuResponse
from utils.usual import get_user_info_from_token
import random

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
    point_id: str = Field(None, alias="point_id")
    address: str = Field(None, alias="address")
    area: str = Field(None, alias="area")
    manager: str = Field(None, alias="manager")


# 设置请求接收字段
class PointManageSchemaIn(ModelSchema):
    class Config:
        model = Point
        model_fields = ['name', 'time', 'longitude', 'latitude', 'area', 'area_id', 'manager',
                        'manager_phone', 'introduction', 'address', 'notes']


# 设置响应字段
class PointManageSchemaOut(ModelSchema):
    class Config:
        model = Point
        model_fields = "__all__"



# 创建Point
@router.post("/point_manage", response=PointManageSchemaOut)
def create_point(request, data: PointManageSchemaIn):
    user_info = get_user_info_from_token(request)
    if user_info['is_superuser']:
        # 如果是超级管理员调用封装的create函数
        point = create(request, data, Point)
        return point
    else:
        # return
        return FuResponse(code=403, msg="当前用户没有修改权限")


# 删除Point
@router.delete("/point_manage/{point_id}")
def delete_point(request, point_id: str):
    user_info = get_user_info_from_token(request)
    if user_info['is_superuser']:
        delete(point_id, Point)
        return {"success": True}
    else:
        return FuResponse(code=403, msg="当前用户没有修改权限")


# 更新Point
@router.put("/point_manage/{point_id}", response=PointManageSchemaOut)
def update_point(request, point_id: str, data: PointManageSchemaIn):
    user_info = get_user_info_from_token(request)
    if user_info['is_superuser']:
        point = update(request, point_id, data, Point)
        return point
    else:
        return FuResponse(code=403, msg="当前用户没有修改权限")


# 获取Point 并分页
@router.get("/point_manage", response=List[PointManageSchemaOut])
@paginate(MyPagination)
def list_point(request, filters: Filters = Query(...)):
    qs = retrieve(request, Point, filters)
    return qs


# 获取所有Point
@router.get("/point_manage/all/list", response=List[PointManageSchemaOut])
def all_list_point(request):
    qs = retrieve(request, Point)
    return qs


# 根据id获取单个Point
@router.get("/point_manage/{point_id}", response=PointManageSchemaOut)
def get_point(request, point_id: str):
    point = get_object_or_404(Point, id=point_id)
    return point


# # 导入
# @router.get("/point/all/export")
# def export_point(request):
#     title_dict = {
#         'name': '名称',
#         'code': '编码',
#         'status': '状态',
#         'sort': '排序',
#     }
#     return export_data(request, Point, PointManageSchemaOut, title_dict)
#
#
# # 导出
# @router.post("/point/all/import")
# def import_point(request, data: ImportSchema):
#     title_dict = {
#         '名称': 'name',
#         '编码': 'code',
#         '状态': 'status',
#         '排序': 'sort',
#     }
#     return import_data(request, Point, PointManageSchemaIn, data, title_dict)
