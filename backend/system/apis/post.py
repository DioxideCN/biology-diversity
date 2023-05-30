# -*- coding: utf-8 -*-
# @Time    : 2022/5/10 21:56
# @Author  : 臧成龙
# @FileName: post.py
# @Software: PyCharm

from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Schema, Field, UploadedFile
from ninja.pagination import paginate
from system.models import Post
from utils.fu_crud import create, delete, update, retrieve, ImportSchema, export_data, import_data
from utils.fu_ninga import MyPagination, FuFilters
router = Router()


class Filters(FuFilters):
    name: str = Field(None, alias="name")
    code: str = Field(None, alias="code")
    status: int = Field(None, alias="status")

    id: str = Field(None, alias="post_id")


class PostSchemaIn(ModelSchema):
    class Config:
        model = Post
        model_fields = ['name', 'code', 'sort', 'status']


class PostSchemaOut(ModelSchema):
    class Config:
        model = Post
        model_fields = "__all__"


@router.post("/post", response=PostSchemaOut)
def create_post(request, data: PostSchemaIn):
    post = create(request, data, Post)
    return post


@router.delete("/post/{post_id}")
def delete_post(request, post_id: int):
    delete(post_id, Post)
    return {"success": True}


@router.put("/post/{post_id}", response=PostSchemaOut)
def update_post(request, post_id: int, data: PostSchemaIn):
    post = update(request, post_id, data, Post)
    return post


@router.get("/post", response=List[PostSchemaOut])
@paginate(MyPagination)
def list_post(request, filters: Filters = Query(...)):
    qs = retrieve(request, Post, filters)
    return qs


@router.get("/post/{post_id}", response=PostSchemaOut)
def get_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return post


@router.get("/post/all/list", response=List[PostSchemaOut])
def all_list_post(request):
    qs = retrieve(request, Post)
    return qs


@router.get("/post/all/export")
def export_post(request):
    title_dict = {
        'name': '名称',
        'code': '编码',
        'status': '状态',
        'sort': '排序',
    }
    return export_data(request, Post, PostSchemaOut, title_dict)


@router.post("/post/all/import")
def import_post(request, data: ImportSchema):
    title_dict = {
        '名称': 'name',
        '编码': 'code',
        '状态': 'status',
        '排序': 'sort',
    }
    return import_data(request, Post, PostSchemaIn, data, title_dict)

