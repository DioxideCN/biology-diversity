from datetime import date, timedelta
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Field
from ninja.files import UploadedFile
from ninja.pagination import paginate
from ninja import File as NinjaFile

from biology.apis import point
from biology.models import RealTime_recognition, Equipment, Areas, Point, RealTimeRecognitionDetail, Animal
from utils.fu_crud import create, delete, update, retrieve, ImportSchema, export_data, import_data
from utils.fu_ninga import MyPagination, FuFilters
from fuadmin.settings import STATIC_URL

import base64, json, os, datetime, logging, requests
from django.test import TestCase

from utils.json_util import get_best_result

router = Router()


# 设置过滤字段 提前将字段转型
class Filters(FuFilters):
    id: int = Field(None, alias="id")
    cn: str = Field(None, alias="cn")
    en: str = Field(None, alias="en")
    type: str = Field(None, alias="type")
    area_id: str = Field(None, alias="area_id")
    point_id: str = Field(None, alias="point_id")
    isExcellent: bool = Field(None, alias="isExcellent")
    isFalse: bool = Field(None, alias="isFalse")
    start_time: date = Field(None, alias="start_time")
    end_time: date = Field(None, alias="end_time")
    equipment_id: str = Field(None, alias="equipment_id")
    equipment_name: str = Field(None, alias="equipment_name")


# 设置请求接收字段
class RealTime_recognitionSchemaIn(ModelSchema):
    class Config:
        model = RealTime_recognition
        model_fields = "__all__"


# 设置响应字段
class RealTime_recognitionSchemaOut(ModelSchema):
    class Config:
        model = RealTime_recognition
        model_fields = "__all__"


# 获取点位信息中历史图片
@router.get("/history/{point_id}")
def get_hispic(request, point_id: str):
    qs = list(RealTime_recognition.objects.filter(point_id=point_id).values('url'))
    qs = qs[0:3]
    data = {
        "history_picture": qs
    }
    return data


# 创建RealTime_recognition
@router.post("/recognition/realtime", response=RealTime_recognitionSchemaOut)
def create_recognition(request, data):
    data_bytes = base64.b64decode(data)
    data_dict = json.load(data_bytes)
    new_data: RealTime_recognitionSchemaIn
    new_data['equipment_id'] = data_dict['deveice_code']
    max = 0
    for item in data_dict['result_text']:
        if item['prob'] > max:
            max = item['prob']
    new_data['degree'] = max
    recognition = create(request, new_data, RealTime_recognition)
    return recognition


# 删除RealTime_recognition
@router.delete("/recognition/realtime/{recognition_id}")
def delete_recognition(request, recognition_id: int):
    delete(recognition_id, RealTime_recognition)
    return {"success": True}


# 更新RealTime_recognition
@router.put("/recognition/realtime/{recognition_id}", response=RealTime_recognitionSchemaOut)
def update_recognition(request, recognition_id: int, data: RealTime_recognitionSchemaIn):
    recognition = update(request, recognition_id, data, RealTime_recognition)
    return recognition


# 获取RealTime_recognition 并分页
@router.get("/recognition/realtime", response=List[RealTime_recognitionSchemaOut])
@paginate(MyPagination)
def list_recognition(request, filters: Filters = Query(...)):
    start_time = filters.start_time
    end_time = filters.end_time
    cn = filters.cn
    filters.cn = ''
    filters.start_time = ''
    filters.end_time = ''
    qs = retrieve(request, RealTime_recognition, filters)
    if start_time is not None and end_time is not None:
        qs = qs.filter(start_time__gte=start_time, end_time__lte=end_time)
    if cn is not None:
        qs = qs.filter(cn__icontains=cn)
    return qs


# 获取所有识别
@router.get("/recognition/realtime/all/list", response=List[RealTime_recognitionSchemaOut])
def all_list_recognition(request):
    qs = retrieve(request, RealTime_recognition)
    return qs


# 根据id获取单个识别
@router.get("/recognition/realtime/{recognition_id}", response=RealTime_recognitionSchemaOut)
def get_recognition(request, recognition_id: int):
    recognition = get_object_or_404(RealTime_recognition, id=recognition_id)
    return recognition


# 根据设备名称获取单个识别
@router.get("/recognition/realtime/{equipment_name}", response=RealTime_recognitionSchemaOut)
def get_recognition_by_equipment_name(request, equipment_name: str):
    recognition = get_object_or_404(RealTime_recognition, name=equipment_name)
    return recognition


# # 根据点位名称获取单个识别
# @router.get("/recognition/realtime/{ponit_name}", response=RealTime_recognitionSchemaOut)
# def get_recognition_by_ponit_name(request, ponit_name: str):
#     recognition = get_object_or_404(RealTime_recognition, name=ponit_name)
#     return recognition


# # 根据区域名称获取单个识别
# @router.get("/recognition/realtime/{area_name}", response=RealTime_recognitionSchemaOut)
# def get_recognition_by_area_name(request, area_name: str):
#     data = point.objects.get(area_name=area_name)
#     ponit_name = data['name']
#     recognition = get_object_or_404(RealTime_recognition, name=ponit_name)
#     return recognition


# 根据起始时间获取单个识别
@router.get("/recognition/realtime", response=RealTime_recognitionSchemaOut)
def get_recognition_by_time(request, start_time: date, end_time: date):
    # recognition = get_object_or_404(RealTime_recognition, datetime=start_time, datetime=end_time)
    recognition = RealTime_recognition.objects.filter(end_time__range=[start_time, end_time])
    return recognition


# 调用第三方接口
@router.post("/detect/result/callback", auth=None)
def callback(request):
    # try:
    # binary_data = file.read()
    # file_name = current_date + '_' + file.name.replace(' ', '_')
    # file_path = os.path.join(STATIC_URL, current_ymd)
    # if not os.path.exists(file_path):
    #     os.makedirs(file_path)
    # file_url = os.path.join(file_path, file_name)
    # with open(file_url, 'wb') as f:
    #     f.write(binary_data)
    identify = base64.b64decode(request.request_data["identify"])
    identify = json.loads(str(identify,'utf-8'))
    callbody = identify["callbody"]
    batch_no = callbody["batch"]
    device_code = callbody["device_code"]
    result_text = callbody["result_text"]
    best_result,animial_list = get_best_result(result_text)
    url = callbody["obs_url"]
    best_cname = best_result["cname"]
    best_prob = best_result["prob"]
    svrCode = best_result["svrCode"]
    start_time = datetime.strptime(callbody["start_time"], "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(callbody["end_time"], "%Y-%m-%d %H:%M:%S")
    point_name,en,gang,order,type,equipment_name= "","","","","",""

    animal = Animal.objects.filter(recognition_id=svrCode).first()
    if animal:
        en = animal.en
        gang = animal.gang
        order = animal.order
        type = f"{gang}-{order}"

    eq = Equipment.objects.filter(equipment_number=device_code).first()
    if eq:
        point_id = eq.point_id
        point_name = eq.point_name
        equipment_name = eq.name
    point = Point.objects.filter(id=point_id).first()
    area_id = point.area_id
    area_name = point.area

    # device = Equipment.objects.get(code=device_code)
    detect_result = RealTime_recognition(equipment_id=device_code, batch=batch_no, cn=best_cname,degree=best_prob,result_text=str(result_text),
                                         url=url,en=en, type=type, ponit_name=point_name, equipment_name=equipment_name,
                                         area_id=area_id, area_name=area_name,
                                         point_id=point_id, point_name=point_name,
                                         start_time=start_time,
                                         end_time=end_time
                                         )
    detect_result.save()

    for animal in animial_list:
        RealTimeRecognitionDetail(name=animal["cname"], recognition_id=animal["svrCode"], recognition_number=animal["num"],
                                  batch_no=batch_no).save()
    return {"success": True}
