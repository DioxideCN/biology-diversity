# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 23:41
# @Author  : 臧成龙
# @FileName: fu_ninga.py
# @Software: PyCharm
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from ninja import NinjaAPI, Schema, ModelSchema
from typing import Any, List

from ninja.orm.metaclass import ModelSchemaMetaclass
from ninja.types import DictStrAny
from ninja.pagination import PaginationBase
from ninja import Field, Query, Router, Schema

from utils.fu_response import FuResponse
from utils.usual import get_user_info_from_token


class FuNinjaAPI(NinjaAPI):
    def create_response(
            self, request: HttpRequest, data: Any, *, status: int = 200, code: int = 2000, msg: str = "success",
    ) -> HttpResponse:
        std_data = {
            "code": code,
            "result": data,
            "message": msg,
            "success": True
        }
        content = self.renderer.render(request, std_data, response_status=status)
        content_type = "{}; charset={}".format(
            self.renderer.media_type, self.renderer.charset
        )

        return HttpResponse(content, status=status, content_type=content_type)


class MyPagination(PaginationBase):
    class Input(Schema):
        pageSize: int = Field(12, gt=0)
        page: int = Field(1, gt=-1)

    class Output(Schema):
        items: List[Any]
        total: int

    def paginate_queryset(
            self,
            queryset: QuerySet,
            pagination: Input,
            **params: DictStrAny,
    ) -> Any:
        offset = pagination.pageSize * (pagination.page - 1)
        limit: int = pagination.pageSize
        return {
            "page": offset,
            "limit": limit,
            "items": queryset[offset: offset + limit],
            "total": self._items_count(queryset),
        }  # noqa: E203


class FuFilters(Schema):
    creator_id: int = Field(None, alias="creator_id")
    belong_dept: int = Field(None, alias="belong_dept")
    belong_dept__in: List[int] = Field(None, alias="belong_dept__in")
