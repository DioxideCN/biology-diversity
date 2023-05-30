#
# from typing import List
#
# from django.shortcuts import get_object_or_404
# from ninja import Router, ModelSchema, Query, Field
# from ninja.pagination import paginate
#
# from biology.models import Areas
# from utils.fu_crud import create, delete, update, retrieve, ImportSchema, export_data, import_data
# from utils.fu_ninga import MyPagination, FuFilters
#
# import json
#
# router = Router()
#
#
# # 设置过滤字段 提前将字段转型
# class Filters(FuFilters):
#     id: int = Field(None, alias="id")
#     name: str = Field(None, alias="name")
#
#
# # 设置请求接收字段
# class AreasSchemaIn(ModelSchema):
#     class Config:
#         model = Areas
#         model_fields = ['name', 'province', 'city', 'district', 'manager', 'manager_phone', 'introduction', 'notes']
#
#
# # 设置响应字段
# class AreasSchemaOut(ModelSchema):
#     class Config:
#         model = Areas
#         model_fields = "__all__"
#
#
# # 创建Areas
# @router.post("/area", response=AreasSchemaOut)
# def create_area(request, data: AreasSchemaIn):
#     # 调用封装的create函数
#     area = create(request, data, Areas)
#     return area
#
#
# # 删除Areas
# @router.delete("/area/{area_id}")
# def delete_area(request, area_id: int):
#     delete(area_id, Areas)
#     return {"success": True}
#
#
# # 更新Areas
# @router.put("/area/{area_id}")
# def update_area(request, area_id: int, data: AreasSchemaIn):
#     area = update(request, area_id, data, Areas)
#     data = {}
#     data['path'] = area.path
#     data['id'] = area.id
#     data['name'] = area.name
#     return {
#         "success": True,
#         "result": data,
#         "code": 200,
#         "message": "success"
#     }
#
#
# # # 获取Areas
# # @router.get("/area", response=List[AreasSchemaOut])
# # def list_area(request, filters: Filters = Query(...)):
# #     qs = retrieve(request, Areas, filters)
# #     return qs
#
#
# # 获取Areas
# @router.get("/area/search")
# def list_area(request, path: str):
#     area = get_object_or_404(Areas, path=path)
#     area.path = json.loads(area.path)
#     data = {}
#     data['path'] = area.path
#     data['id'] = area.id
#     data['name'] = area.name
#     return {
#         "success": True,
#         "result": data,
#         "code": 200,
#         "message": "success"
#     }
#
#
# # 获取所有动物
# @router.get("/area/all/list")
# def all_list_area(request):
#     qs = retrieve(request, Areas)
#     areas = []
#     for unit in qs:
#         area = {}
#         area['id'] = unit.id
#         area['name'] = unit.name
#         area['path'] = json.loads(unit.path)
#         areas.append(area)
#     return {
#         "success": True,
#         "result": areas,
#         "code": 200,
#         "message": "success"
#     }
#
#
# # 根据id获取单个动物
# @router.get("/area/{area_id}", response=AreasSchemaOut)
# def get_area(request, area_id: int):
#     area = get_object_or_404(Areas, id=area_id)
#     area.path = json.loads(area.path)
#     # return area
#     data = {}
#     data['path'] = area.path
#     data['id'] = area.id
#     data['name'] = area.name
#     return {
#         "success": True,
#         "result": data,
#         "code": 200,
#         "message": "success"
#     }
#
#
# # # 导入
# # @router.get("/area/all/export")
# # def export_area(request):
# #     title_dict = {
# #         'name': '名称',
# #         'code': '编码',
# #         'status': '状态',
# #         'sort': '排序',
# #     }
# #     return export_data(request, Areas, AreasSchemaOut, title_dict)
# #
# #
# # # 导出
# # @router.post("/area/all/import")
# # def import_area(request, data: ImportSchema):
# #     title_dict = {
# #         '名称': 'name',
# #         '编码': 'code',
# #         '状态': 'status',
# #         '排序': 'sort',
# #     }
# #     return import_data(request, Areas, AreasSchemaIn, data, title_dict)
