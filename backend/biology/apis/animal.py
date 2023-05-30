
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Field
from ninja.pagination import paginate

from biology.models import Animal
from utils.fu_crud import create, delete, update, retrieve, ImportSchema, export_data, import_data
from utils.fu_ninga import MyPagination, FuFilters

router = Router()


# 设置过滤字段 提前将字段转型
class Filters(FuFilters):
    id: int = Field(None, alias="id")
    name: str = Field(None, alias="name")
    cn: str = Field(None, alias="cn")
    ladin: str = Field(None, alias="ladin")
    recognition_id: str = Field(None, alias="recognition_id")


# 设置请求接收字段
class AnimalSchemaIn(ModelSchema):
    class Config:
        model = Animal
        model_fields = ['cn', 'en', 'ladin', 'name_man', 'name_date', 'other_name', 'is_protected',
                        'protection_level', 'big_class', 'sub_class', 'kingdom', 'phylum', 'subphylum',
                        'gang', 'subclass', 'order', 'suborder', 'family', 'subfamily', 'species',
                        'subspecies', 'tribe', 'genus', 'grow', 'url', 'introduction', 'notes',
                        'k_code', 'k_name', 'recognition_id']


# 设置响应字段
class AnimalSchemaOut(ModelSchema):
    class Config:
        model = Animal
        model_fields = "__all__"


# 创建Animal
@router.post("/animal", response=AnimalSchemaOut)
def create_animal(request, data: AnimalSchemaIn):
    # 调用封装的create函数
    animal = create(request, data, Animal)
    return animal


# 删除Animal
@router.delete("/animal/{animal_id}")
def delete_animal(request, animal_id: int):
    delete(animal_id, Animal)
    return {"success": True}


# 更新Animal
@router.put("/animal/{animal_id}", response=AnimalSchemaOut)
def update_animal(request, animal_id: int, data: AnimalSchemaIn):
    animal = update(request, animal_id, data, Animal)
    return animal


# 获取Animal 并分页
@router.get("/animal", response=List[AnimalSchemaOut])
@paginate(MyPagination)
def list_animal(request, filters: Filters = Query(...)):
    qs = retrieve(request, Animal, filters)
    return qs


# 获取所有动物
@router.get("/animal/all/list", response=List[AnimalSchemaOut])
def all_list_animal(request):
    qs = retrieve(request, Animal)
    return qs


# 根据id获取单个动物
@router.get("/animal/{animal_id}", response=AnimalSchemaOut)
def get_animal(request, animal_id: int):
    animal = get_object_or_404(Animal, id=animal_id)
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
