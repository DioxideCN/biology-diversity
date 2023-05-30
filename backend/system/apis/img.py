import os
from typing import List
from urllib.parse import unquote
from conf.env import STATIC_FILE_PATH, STATIC_DOMAIN
from django.http import StreamingHttpResponse, FileResponse, JsonResponse
from ninja.files import UploadedFile
from ninja import File as NinjaFile
from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Schema, Field
from ninja.pagination import paginate
from datetime import datetime
from utils.string_util import random_str
from ninja.testing.client import build_absolute_uri

from fuadmin.settings import STATIC_URL, BASE_DIR
from system.models import File
from utils.fu_crud import create, delete, update, retrieve
from utils.fu_ninga import MyPagination, FuFilters
from utils.oss_utils import update_fil_file

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


@router.post("/uploadImage",auth=None)
def upload(request, file: UploadedFile = NinjaFile(...)):
    binary_data = file.read()
    suffix = os.path.splitext(file.name)[1]
    if suffix.lower() == '.jpeg' or suffix.lower() == ".png" or suffix.lower() == ".jpg":
        current_ymd = datetime.now().strftime('%Y-%m-%d')
        file_name = (random_str(24)).lower() + suffix
        file_path = os.path.join(STATIC_FILE_PATH, "animalPic", current_ymd)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file_url = os.path.join(file_path, file_name)
        with open(file_url, 'wb') as f:
            f.write(binary_data)

        file_url = file_url.replace(STATIC_FILE_PATH, STATIC_DOMAIN)
        data = {
            'status': "success",
            'msg': "",
            'name': file.name,
            'size': file.size,
            'url': file_url,

        }
    else:
        data = {
            'status': "error",
            'msg': "上传文件格式错误，只允许上传jpg、png、jpeg格式"

        }
    return JsonResponse(data)
