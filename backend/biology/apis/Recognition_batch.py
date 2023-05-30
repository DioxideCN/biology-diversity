from datetime import date, timedelta
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Field
from ninja.pagination import paginate

from biology.models import Recognition_batch
from utils.fu_crud import delete, update, retrieve, ImportSchema, export_data, import_data
from utils.fu_ninga import MyPagination, FuFilters

from django.utils import timezone
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
        data['id'] = 'IIBM' + date + '000' + str(random_number)
    elif random_number < 100:
        data['id'] = 'IIBM' + date + '00' + str(random_number)
    elif random_number < 1000:
        data['id'] = 'IIBM' + date + '0' + str(random_number)
    else:
        data['id'] = 'IIBM' + date + str(random_number)
    query_set = model.objects.create(**data)
    return query_set


# 设置过滤字段 提前将字段转型
class Filters(FuFilters):
    id: str = Field(None, alias="id")
    start_time: str = Field(None, alias="start_time")
    end_time: str = Field(None, alias="end_time")


# 设置请求接收字段
class Recognition_batchSchemaIn(ModelSchema):
    class Config:
        model = Recognition_batch
        model_fields = "__all__"


# 设置响应字段
class Recognition_batchSchemaOut(ModelSchema):
    class Config:
        model = Recognition_batch
        model_fields = "__all__"


# 创建Recognition_batch
@router.post("/recognition/batch", response=Recognition_batchSchemaOut)
def create_recognition(request, data: Recognition_batchSchemaIn):
    # 调用封装的create函数
    recognition = create(request, data, Recognition_batch)
    return recognition


# 删除Recognition_batch
@router.delete("/recognition/batch/{batch_id}")
def delete_recognition(request, batch_id: str):
    delete(batch_id, Recognition_batch)
    return {"success": True}


# 更新Recognition_batch
@router.put("/recognition/batch/{batch_id}", response=Recognition_batchSchemaOut)
def update_recognition(request, batch_id: str, data: Recognition_batchSchemaIn):
    recognition = update(request, batch_id, data, Recognition_batch)
    return recognition


# 获取Recognition_batch 并分页
@router.get("/recognition/batch", response=List[Recognition_batchSchemaOut])
@paginate(MyPagination)
def list_recognition(request, filters: Filters = Query(...)):
    qs = retrieve(request, Recognition_batch, filters)
    return qs


# 根据时间段获取Recognition_batch 并分页
@router.get("/recognition/batch/time", response=List[Recognition_batchSchemaOut])
@paginate(MyPagination)
def time_recognition(request, start_time: date = None, end_time: date = None):
    Recognition_batch.recognition_number = Recognition_batch.objects.all.count()
    last_time = end_time + timedelta(days=1)
    qs = retrieve(request, Recognition_batch).filter(time_range=(start_time, last_time)).distinct('name')
    return qs


# 获取所有识别
@router.get("/recognition/batch/all/list", response=List[Recognition_batchSchemaOut])
def all_list_recognition(request):
    qs = retrieve(request, Recognition_batch)
    return qs


# 根据id获取单个识别
@router.get("/recognition/batch/{batch_id}", response=Recognition_batchSchemaOut)
def get_recognition(request, batch_id: int):
    recognition = get_object_or_404(Recognition_batch, id=batch_id)
    return recognition