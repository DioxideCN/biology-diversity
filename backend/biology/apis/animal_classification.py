
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Field
from ninja.pagination import paginate

from biology.models import Animal_classification
from utils.fu_crud import create, delete, update, retrieve, ImportSchema, export_data, import_data
from utils.fu_ninga import MyPagination, FuFilters

router = Router()


# 设置过滤字段 提前将字段转型
class Filters(FuFilters):
    id: int = Field(None, alias="id")
    name: str = Field(None, alias="name")
    animal_id: str = Field(None, alias="animal_id")
    type: str = Field(None, alias="type")



# 设置请求接收字段
class AnimalSchemaIn(ModelSchema):
    class Config:
        model = Animal_classification
        model_fields = ['name', 'notes', 'type', 'animal_id']


# 设置响应字段
class AnimalSchemaOut(ModelSchema):
    class Config:
        model = Animal_classification
        model_fields = "__all__"


# 创建Animal
@router.post("/animal_classification", response=AnimalSchemaOut)
def create_animal(request, data: AnimalSchemaIn):
    # 调用封装的create函数
    animal = create(request, data, Animal_classification)
    return animal


# 删除Animal
@router.delete("/animal_classification/{animal_id}")
def delete_animal(request, animal_id: int):
    delete(animal_id, Animal_classification)
    return {"success": True}


# 更新Animal
@router.put("/animal_classification/{animal_id}", response=AnimalSchemaOut)
def update_animal(request, animal_id: int, data: AnimalSchemaIn):
    animal = update(request, animal_id, data, Animal_classification)
    return animal


# 获取Animal 并分页
@router.get("/animal_classification", response=List[AnimalSchemaOut])
@paginate(MyPagination)
def list_animal(request, filters: Filters = Query(...)):
    qs = retrieve(request, Animal_classification, filters)
    return qs


# 获取所有动物
@router.get("/animal_classification/all/list", response=List[AnimalSchemaOut])
def all_list_animal(request):
    qs = retrieve(request, Animal_classification)
    return qs


# 根据id获取单个动物
@router.get("/animal_classification/{animal_id}", response=AnimalSchemaOut)
def get_animal(request, animal_id: int):
    animal = get_object_or_404(Animal_classification, id=animal_id)
    return animal


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
