from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Field

from biology.models import Point
from utils.fu_crud import create, delete, update, retrieve, ImportSchema, export_data, import_data
from utils.fu_ninga import MyPagination, FuFilters

import json

router = Router()


# 设置过滤字段 提前将字段转型
class Filters(FuFilters):
    id: int = Field(None, alias="id")
    path: str = Field(None, alias="path")


# 设置请求接收字段
class PointSchemaIn(ModelSchema):
    class Config:
        model = Point
        model_fields = ['name', 'time', 'longitude', 'latitude', 'area', 'area_id', 'manager',
                        'manager_phone', 'introduction', 'address', 'notes']


# 设置响应字段
class PointSchemaOut(ModelSchema):
    class Config:
        model = Point
        model_fields = "__all__"


# 创建Point
@router.post("/point", response=PointSchemaOut)
def create_point(request, data: PointSchemaIn):
    # 调用封装的create函数
    point = create(request, data, Point)
    return point


# 删除Point
@router.delete("/point/{point_id}")
def delete_point(request, point_id: int):
    delete(point_id, Point)
    return {"success": True}


# 更新Point
@router.put("/point/{point_id}", response=PointSchemaOut)
def update_point(request, point_id: int, data: PointSchemaIn):
    point = update(request, point_id, data, Point)
    return point


# 获取Point
@router.get("/point/search")
def list_area(request, path: str):
    point = get_object_or_404(Point, path=path)
    point.path = json.loads(point.path)
    data = {}
    data['path'] = point.path
    data['id'] = point.id
    data['name'] = point.name
    return {
        "success": True,
        "result": data,
        "code": 200,
        "message": "success"
    }


# 获取所有动物
@router.get("/point/all/list")
def all_list_point(request):
    qs = retrieve(request, Point)
    points = []
    for unit in qs:
        point = {}
        point['id'] = unit.id
        point['name'] = unit.name
        point['path'] = json.loads(unit.path)
        points.append(point)
    return {
        "success": True,
        "result": points,
        "code": 200,
        "message": "success"
    }


# 根据id获取单个
@router.get("/point/{point_id}", response=PointSchemaOut)
def get_point(request, point_id: int):
    point = get_object_or_404(Point, id=point_id)
    point.path = json.loads(point.path)
    data = {}
    data['path'] = point.path
    data['id'] = point.id
    data['name'] = point.name
    return {
        "success": True,
        "result": data,
        "code": 200,
        "message": "success"
    }

# # 导入
# @router.get("/point/all/export")
# def export_point(request):
#     title_dict = {
#         'name': '名称',
#         'code': '编码',
#         'status': '状态',
#         'sort': '排序',
#     }
#     return export_data(request, Point, PointSchemaOut, title_dict)
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
#     return import_data(request, Point, PointSchemaIn, data, title_dict)
