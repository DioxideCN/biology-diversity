import logging
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Field, Schema
from ninja.pagination import paginate

from biology.models import Equipment, RealTime_recognition, Point, Animal, RealTimeRecognitionDetail
from utils.fu_crud import create, delete, update, retrieve, ImportSchema, export_data, import_data
from utils.fu_ninga import MyPagination, FuFilters

from django.utils import timezone
from django.utils.timezone import now, timedelta
import datetime, json
from datetime import date
from django.db.models import Avg, Max, Min, Count, Sum
from django.http import JsonResponse
from django.core import serializers
from utils.usual import get_user_info_from_token
import random

router = Router()


# 设置过滤字段 提前将字段转型
class Filters(FuFilters):
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    status: str = Field(None, alias="status")
    equipment_id: str = Field(None, alias="equipment_id")
    point_id: str = Field(None, alias="point_id")
    equipment_number: str = Field(None, alias="equipment_number")


# 设置请求接收字段
class EquipmentSchemaIn(ModelSchema):
    class Config:
        model = Equipment
        model_fields = "__all__"


# 设置响应字段
class EquipmentSchemaOut(ModelSchema):
    class Config:
        model = Equipment
        model_fields = "__all__"


class RealTime_recognitionSchemaOut(ModelSchema):
    class Config:
        model = RealTime_recognition
        model_fields = "__all__"


# 创建Equipment
@router.post("/equipment", response=EquipmentSchemaOut)
def create_equipment(request, data: EquipmentSchemaIn):
    # 调用封装地create函数
    equipment = create(request, data, Equipment)
    return equipment


# 删除Equipment
@router.delete("/equipment/{equipment_id}")
def delete_equipment(request, equipment_id: str):
    delete(equipment_id, Equipment)
    return {"success": True}


# 更新Equipment
@router.put("/equipment/{equipment_id}", response=EquipmentSchemaOut)
def update_equipment(request, equipment_id: str, data: EquipmentSchemaIn):
    equipment = update(request, equipment_id, data, Equipment)
    return equipment


# 获取Equipment 并分页
@router.get("/equipment", response=List[EquipmentSchemaOut])
@paginate(MyPagination)
def list_equipment(request, filters: Filters = Query(...)):
    qs = retrieve(request, Equipment, filters)
    return qs


# 数据大屏
@router.get("/data")
def data_screen(request):
    qs = {}
    today = timezone.now().date()
    yesterday = timezone.now().date() + timedelta(days=-1)
    qs['equipment_online_number'] = Equipment.objects.filter(status='在线').count()
    qs['equipment_outline_number'] = Equipment.objects.exclude(status='在线').count()
    qs['recognition_number'] = RealTimeRecognitionDetail.objects.count()
    qs['recognition_td_number'] = RealTimeRecognitionDetail.objects.filter(
        update_datetime__gte=str(today) + ' 00:00:00').count()
    qs['recognition_yd_number'] = RealTimeRecognitionDetail.objects.filter(
        update_datetime__gte=str(yesterday) + ' 00:00:00',
        update_datetime__lte=str(yesterday) + ' 23:59:59').count()
    return qs


# 识别总量统计
@router.get("/data/trend")
def data_screen(request):
    qs = {}
    year = timezone.now().year
    for i in range(1, 13):
        if i < 10:
            month = str(year) + '-0' + str(i)
        else:
            month = str(year) + '-' + str(i)
        qs[i] = RealTimeRecognitionDetail.objects.filter(update_datetime__startswith=month).count()
    return qs


# 高清图片
@router.get("/data/image")
def data_screen(request):
    qs = list(RealTime_recognition.objects.filter(isExcellent="True").values('url'))
    qs = qs[0:3]
    data = {
        'qs': qs
    }
    return data


# 识别动物总量
@router.get("/data/number")
def data_screen(request, start_time: str = None, end_time: str = None):
    if start_time is None and end_time is None:
        qs = list(RealTimeRecognitionDetail.objects.all().values('name').annotate(
            count=Count('name')).order_by('-count'))
    else:
        qs = list(RealTimeRecognitionDetail.objects.filter(update_datetime__gte=start_time,
                                                           update_datetime__lte=end_time).values('name').annotate(
            count=Count('name')).order_by('-count'))
    data = {
        'queryset': qs
    }
    return data


# 重点物种监控
@router.get("/data/important")
def data_screen(request):
    qs = {}
    today = timezone.now().date().strftime("%Y-%m-%d")
    yesterday = (timezone.now().date() + timedelta(days=-1)).strftime("%Y-%m-%d")
    animal = Animal.objects.filter(is_protected="True")
    name = animal[0].cn
    qs['name'] = name
    qs['today'] = RealTime_recognition.objects.filter(cn=name, update_datetime__gte=str(today) + ' 00:00:00').count()
    qs['yesterday'] = RealTime_recognition.objects.filter(cn=name, update_datetime__gte=str(yesterday) + ' 00:00:00',
                                                          update_datetime__lte=str(yesterday) + ' 23:59:59').count()
    qs['total'] = RealTime_recognition.objects.filter(cn=name).count()
    qs['url'] = animal[0].url
    return qs


# 视频直播
@router.get("/data/video")
def data_screen(request):
    qs = list(Equipment.objects.filter(is_screenShow="True").values('living_url', 'name'))
    qs = qs[0:2]
    # equipment = Equipment.objects.get(is_screenShow="True")
    # info = {'name': equipment['name'], 'living_url': equipment['living_url']}
    data = {
        'qs': qs
    }
    return data



# 获取Equipment 并分页
@router.get("/equipments", response=List[RealTime_recognitionSchemaOut])
@paginate(MyPagination)
def list_equipment(request, filters: Filters = Query(...)):
    queryset = []
    qs = retrieve(request, Equipment, filters)
    for item in qs:
        list1 = RealTime_recognition.objects.filter(equipment_id=item.id)
        queryset.extend(list1)
    return queryset


# 获取所有Equipment
@router.get("/equipment/all/list", response=List[EquipmentSchemaOut])
def all_list_equipment(request):
    qs = retrieve(request, Equipment)
    return qs


# 根据id获取单个Equipment
@router.get("/equipment/{equipment_id}", response=EquipmentSchemaOut)
def get_equipment(request, equipment_id: str):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    return equipment


@router.post("/equipment/status/synchronization", auth=None)
def synchronization_status(request):
    device_code = request.request_data["device_code"]
    status = request.request_data["status"]
    logging.info(f"Synchronization status:{status},device_code:{device_code}")
    equipment = Equipment.objects.filter(equipment_number=device_code).first()
    if equipment:
        if status == "0":
            equipment.status="在线"
        else:
            equipment.status = "离线"
        equipment.save()