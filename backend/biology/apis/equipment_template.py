
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Field
from ninja.pagination import paginate

from biology.models import EquipmentTemplate
from utils.fu_crud import create, delete, update, retrieve, ImportSchema, export_data, import_data
from utils.fu_ninga import MyPagination, FuFilters

router = Router()


# 设置过滤字段 提前将字段转型
class Filters(FuFilters):
    id: int = Field(None, alias="id")
    name: str = Field(None, alias="name")
    status: str = Field(None, alias="status")


# 设置请求接收字段
class TemplateSchemaIn(ModelSchema):
    class Config:
        model = EquipmentTemplate
        model_fields = "__all__"


# 设置响应字段
class TemplateSchemaOut(ModelSchema):
    class Config:
        model = EquipmentTemplate
        model_fields = "__all__"


# 创建Template
@router.post("/template", response=TemplateSchemaOut)
def create_template(request, data: TemplateSchemaIn):
    # 调用封装的create函数
    template = create(request, data, EquipmentTemplate)
    return template


# 删除Template
@router.delete("/template/{template_id}")
def delete_template(request, template_id: int):
    delete(template_id, EquipmentTemplate)
    return {"success": True}


# 更新Template
@router.put("/template/{template_id}", response=TemplateSchemaOut)
def update_template(request, template_id: int, data: TemplateSchemaIn):
    template = update(request, template_id, data, EquipmentTemplate)
    return template


# 获取Template 并分页
@router.get("/template", response=List[TemplateSchemaOut])
@paginate(MyPagination)
def list_template(request, filters: Filters = Query(...)):
    qs = retrieve(request, EquipmentTemplate, filters)
    return qs


# 获取所有Template
@router.get("/template/all/list", response=List[TemplateSchemaOut])
def all_list_template(request):
    qs = retrieve(request, EquipmentTemplate)
    return qs


# 根据id获取单个Template
@router.get("/template/{template_id}", response=TemplateSchemaOut)
def get_template(request, template_id: int):
    template = get_object_or_404(EquipmentTemplate, id=template_id)
    return template

