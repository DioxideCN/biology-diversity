# -*- coding: utf-8 -*-
# @Time    : 2022/6/07 00:56
# @Author  : 臧成龙
# @FileName: file.py
# @Software: PyCharm
import os
from typing import List
from urllib.parse import unquote

from django.http import StreamingHttpResponse, FileResponse, JsonResponse
from ninja.files import UploadedFile
from ninja import File as NinjaFile
from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Schema, Field
from ninja.pagination import paginate
from datetime import datetime

from ninja.testing.client import build_absolute_uri

from fuadmin.settings import STATIC_URL, BASE_DIR
from system.models import File
from utils.fu_crud import create, delete, update, retrieve
from utils.fu_ninga import MyPagination, FuFilters

router = Router()


class Filters(FuFilters):
    name: str = Field(None, alias="name")


class SchemaIn(Schema):
    name: str = Field(None, alias="name")
    url: str = Field(None, alias="url")


class SchemaOut(ModelSchema):
    class Config:
        model = File
        model_fields = "__all__"


@router.delete("/file/{file_id}")
def delete_file(request, file_id: int):
    delete(file_id, File)
    return {"success": True}


@router.get("/file", response=List[SchemaOut])
@paginate(MyPagination)
def list_file(request, filters: Filters = Query(...)):
    qs = retrieve(request, File, filters)
    return qs


@router.get("/file/{file_id}", response=SchemaOut)
def get_file(request, file_id: int):
    qs = get_object_or_404(File, id=file_id)
    return qs


@router.get("/file/all/list", response=List[SchemaOut])
def all_list_role(request):
    qs = retrieve(request, File)
    return qs


@router.post("/upload", response=SchemaOut)
def upload(request, file: UploadedFile = NinjaFile(...)):
    binary_data = file.read()
    current_date = datetime.now().strftime('%Y%m%d%H%M%S%f')
    current_ymd = datetime.now().strftime('%Y%m%d')
    file_name = current_date + '_' + file.name.replace(' ', '_')
    file_path = os.path.join(STATIC_URL, current_ymd)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_url = os.path.join(file_path, file_name)
    with open(file_url, 'wb') as f:
        f.write(binary_data)
    # print(str(request.get_host))
    # file_url = request.get_host + file_url
    # file_url = os.path.join('http://', str(request.get_host()), file_url)
    data = {
        'name': file.name,
        'size': file.size,
        'save_name': file_name,
        'url': file_url,
    }
    qs = create(request, data, File)
    return qs


@router.post("/download")
def create_post(request, data: SchemaIn):
    filePath = str(BASE_DIR) + unquote(data.url)
    r = FileResponse(open(filePath, "rb"), as_attachment=True)
    return r
