from datetime import date, timedelta
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Field
from ninja.pagination import paginate

from biology.models import Recognition
from utils.fu_crud import create, delete, update, retrieve, ImportSchema, export_data, import_data
from utils.fu_ninga import MyPagination, FuFilters

router = Router()


# 设置过滤字段 提前将字段转型
class Filters(FuFilters):
    id: int = Field(None, alias="id")
    name: str = Field(None, alias="name")
    EnglishName: str = Field(None, alias="EnglishName")
    type: str = Field(None, alias="type")
    result: bool = Field(None, alias="result")
    isExcellent: bool = Field(None, alias="isExcellent")


# 设置请求接收字段
class RecognitionSchemaIn(ModelSchema):
    class Config:
        model = Recognition
        model_fields = ['name', 'EnglishName', 'type', 'recognition_number', 'result', 'degree', 'time', 'isExcellent',
                        'url', 'place', 'equipment', 'reserve', 'fileType']


# 设置响应字段
class RecognitionSchemaOut(ModelSchema):
    class Config:
        model = Recognition
        model_fields = "__all__"


# 创建Recognition
@router.post("/recognition", response=RecognitionSchemaOut)
def create_recognition(request, data: RecognitionSchemaIn):
    # 调用封装的create函数
    recognition = create(request, data, Recognition)
    return recognition


# 删除Recognition
@router.delete("/recognition/{recognition_id}")
def delete_recognition(request, recognition_id: int):
    delete(recognition_id, Recognition)
    return {"success": True}


# 更新Recognition
@router.put("/recognition/{recognition_id}", response=RecognitionSchemaOut)
def update_recognition(request, recognition_id: int, data: RecognitionSchemaIn):
    recognition = update(request, recognition_id, data, Recognition)
    return recognition


# 获取Recognition 并分页
@router.get("/recognition", response=List[RecognitionSchemaOut])
@paginate(MyPagination)
def list_recognition(request, filters: Filters = Query(...)):
    qs = retrieve(request, Recognition, filters)
    return qs


# 根据时间段获取Recognition 并分页
@router.get("/recognition/time", response=List[RecognitionSchemaOut])
@paginate(MyPagination)
def time_recognition(request, start_time: date = None, end_time: date = None):
    Recognition.recognition_number = Recognition.objects.all.count()
    last_time = end_time + timedelta(days=1)
    qs = retrieve(request, Recognition).filter(time_range=(start_time, last_time)).distinct('name')
    return qs


# 获取所有识别
@router.get("/recognition/all/list", response=List[RecognitionSchemaOut])
def all_list_recognition(request):
    qs = retrieve(request, Recognition)
    return qs


# 根据id获取单个识别
@router.get("/recognition/{recognition_id}", response=RecognitionSchemaOut)
def get_recognition(request, recognition_id: int):
    recognition = get_object_or_404(Recognition, id=recognition_id)
    return recognition