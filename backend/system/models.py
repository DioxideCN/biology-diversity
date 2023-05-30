import hashlib
import os
import logging
import datetime
import time
from random import randrange

from captcha.models import MAX_RANDOM_KEY
from django.utils import timezone
from captcha.conf import settings as captcha_settings

from django.utils.encoding import smart_str as smart_text
from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.models import CoreModel

STATUS_CHOICES = (
    (0, "禁用"),
    (1, "启用"),
)


class Users(AbstractUser, CoreModel):
    username = models.CharField(max_length=150, unique=True, db_index=True, verbose_name='用户账号', help_text="用户账号")
    email = models.EmailField(max_length=255, verbose_name="邮箱", null=True, blank=True, help_text="邮箱")
    mobile = models.CharField(max_length=255, verbose_name="电话", null=True, blank=True, help_text="电话")
    avatar = models.TextField(verbose_name="头像", null=True, blank=True, help_text="头像")
    name = models.CharField(max_length=40, verbose_name="姓名", help_text="姓名")
    status = models.BooleanField(default=True, verbose_name="状态", help_text="状态")
    GENDER_CHOICES = (
        (0, "女"),
        (1, "男"),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1, verbose_name="性别", null=True, blank=True,
                                 help_text="性别")
    USER_TYPE = (
        (0, "后台用户"),
        (1, "前台用户"),
    )
    user_type = models.IntegerField(choices=USER_TYPE, default=0, verbose_name="用户类型", null=True, blank=True,
                                    help_text="用户类型")
    post = models.ManyToManyField(to='Post', verbose_name='关联岗位', db_constraint=False, help_text="关联岗位")
    role = models.ManyToManyField(to='Role', verbose_name='关联角色', db_constraint=False, help_text="关联角色")
    dept = models.ForeignKey(to='Dept', verbose_name='所属部门', on_delete=models.SET_NULL, db_constraint=False, null=True,
                             blank=True, help_text="关联部门")
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    login_sta = models.CharField(u'登录是否锁定', max_length=2, default=0)
    login_suo = models.DateTimeField(u'登录锁定时间', default="2000-01-01 00:00:00")
    pass_errnum = models.IntegerField(u'用户密码输入次数', default=0)

    class Meta:
        db_table = "system_users"
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)


class Post(CoreModel):
    name = models.CharField(null=False, max_length=64, verbose_name="岗位名称", help_text="岗位名称")
    code = models.CharField(max_length=32, verbose_name="岗位编码", help_text="岗位编码")
    STATUS_CHOICES = (
        (0, "离职"),
        (1, "在职"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="岗位状态", help_text="岗位状态")

    class Meta:
        db_table = "system_post"
        verbose_name = '岗位表'
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class Role(CoreModel):
    name = models.CharField(max_length=64, verbose_name="角色名称", help_text="角色名称")
    code = models.CharField(max_length=64, unique=True, verbose_name="角色编码", help_text="角色编码")
    # key = models.CharField(max_length=64, unique=True, verbose_name="权限字符", help_text="权限字符")
    status = models.BooleanField(default=True, verbose_name="角色状态", help_text="角色状态")
    admin = models.BooleanField(default=False, verbose_name="是否为admin", help_text="是否为admin")
    DATASCOPE_CHOICES = (
        (0, "仅本人数据权限"),
        (1, "本部门数据权限"),
        (2, "本部门及以下数据权限"),
        (3, "全部数据权限"),
        (4, "自定数据权限"),
    )
    data_range = models.IntegerField(default=0, choices=DATASCOPE_CHOICES, verbose_name="数据权限范围", help_text="数据权限范围")
    dept = models.ManyToManyField(to='Dept', verbose_name='数据权限-关联部门', db_constraint=False, help_text="数据权限-关联部门")
    menu = models.ManyToManyField(to='Menu', verbose_name='关联菜单', db_constraint=False, help_text="关联菜单")
    permission = models.ManyToManyField(to='MenuButton', verbose_name='关联菜单的接口按钮', db_constraint=False,
                                        help_text="关联菜单的接口按钮")

    class Meta:
        db_table = 'system_role'
        verbose_name = '角色表'
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class Dept(CoreModel):
    name = models.CharField(max_length=64, verbose_name="部门名称", help_text="部门名称")
    owner = models.CharField(max_length=32, verbose_name="负责人", null=True, blank=True, help_text="负责人")
    phone = models.CharField(max_length=32, verbose_name="联系电话", null=True, blank=True, help_text="联系电话")
    email = models.EmailField(max_length=32, verbose_name="邮箱", null=True, blank=True, help_text="邮箱")
    status = models.BooleanField(default=True, verbose_name="部门状态", null=True, blank=True,
                                 help_text="部门状态")
    parent = models.ForeignKey(to='Dept', on_delete=models.PROTECT, default=None, verbose_name="上级部门",
                               db_constraint=False, null=True, blank=True, help_text="上级部门")

    class Meta:
        db_table = "system_dept"
        verbose_name = '部门表'
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class Button(CoreModel):
    name = models.CharField(max_length=64, unique=True, verbose_name="权限名称", help_text="权限名称")
    code = models.CharField(max_length=64, unique=True, verbose_name="权限值", help_text="权限值")
    status = models.BooleanField(default=True, verbose_name="按钮状态", null=True, blank=True, help_text="按钮状态")

    class Meta:
        db_table = "system_button"
        verbose_name = '权限标识表'
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class Menu(CoreModel):
    parent = models.ForeignKey(to='Menu', on_delete=models.CASCADE, verbose_name="上级菜单", null=True, blank=True,
                               db_constraint=False, help_text="上级菜单")
    icon = models.CharField(max_length=64, default='ant-design:book-outlined', verbose_name="菜单图标", help_text="菜单图标")
    title = models.CharField(max_length=64, verbose_name="菜单名称", help_text="菜单名称")
    permission = models.CharField(max_length=64, null=True, blank=True, verbose_name="权限标识", help_text="权限标识")
    ISLINK_CHOICES = (
        (0, "否"),
        (1, "是"),
    )
    is_ext = models.BooleanField(default=False, verbose_name="是否外链", help_text="是否外链")

    TYPE_CHOICES = (
        (0, "目录"),
        (1, "菜单"),
    )
    type = models.IntegerField(choices=TYPE_CHOICES, verbose_name="是否目录", help_text="是否目录")
    path = models.CharField(max_length=128, verbose_name="路由地址", null=True, blank=True, help_text="路由地址")
    redirect = models.CharField(max_length=128, verbose_name="重定向地址", null=True, blank=True, help_text="重定向地址")

    component = models.CharField(max_length=128, verbose_name="组件地址", null=True, blank=True, help_text="组件地址")
    name = models.CharField(max_length=50, verbose_name="组件名称", null=True, blank=True, help_text="组件名称")
    status = models.BooleanField(default=True, blank=True, verbose_name="菜单状态", help_text="菜单状态")
    keepalive = models.BooleanField(default=False, blank=True, verbose_name="是否页面缓存", help_text="是否页面缓存")
    hide_menu = models.BooleanField(default=False, blank=True, verbose_name="侧边栏中是否隐藏", help_text="侧边栏中是否隐藏")

    class Meta:
        db_table = "system_menu"
        verbose_name = '菜单表'
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class MenuButton(CoreModel):
    menu = models.ForeignKey(to="Menu", db_constraint=False, related_name="menuPermission", on_delete=models.CASCADE,
                             verbose_name="关联菜单", help_text='关联菜单')
    name = models.CharField(max_length=64, verbose_name="名称", help_text="名称")
    code = models.CharField(max_length=64, verbose_name="权限值", help_text="权限值")
    api = models.CharField(max_length=200, verbose_name="接口地址", help_text="接口地址")
    METHOD_CHOICES = (
        (0, "GET"),
        (1, "POST"),
        (2, "PUT"),
        (3, "DELETE"),
    )
    method = models.IntegerField(default=0, verbose_name="接口请求方法", null=True, blank=True, help_text="接口请求方法")

    class Meta:
        db_table = "system_menu_button"
        verbose_name = '菜单权限表'
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class Dict(CoreModel):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="字典名称", help_text="字典名称")
    code = models.CharField(max_length=100, blank=True, null=True, verbose_name="编码", help_text="编码")
    status = models.BooleanField(default=True, blank=True, verbose_name="状态", help_text="状态")
    remark = models.CharField(max_length=2000, blank=True, null=True, verbose_name="备注", help_text="备注")

    class Meta:
        db_table = 'system_dict'
        verbose_name = "字典表"
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class DictItem(CoreModel):
    label = models.CharField(max_length=100, blank=True, null=True, verbose_name="显示名称", help_text="显示名称")
    value = models.CharField(max_length=100, blank=True, null=True, verbose_name="实际值", help_text="实际值")
    status = models.BooleanField(default=True, blank=True, verbose_name="状态", help_text="状态")
    dict = models.ForeignKey(to="Dict", db_constraint=False, related_name="dictItem", on_delete=models.CASCADE, help_text="字典")
    remark = models.CharField(max_length=2000, blank=True, null=True, verbose_name="备注", help_text="备注")

    class Meta:
        db_table = 'system_dict_item'
        verbose_name = "字典表详情表"
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class CategoryDict(CoreModel):
    label = models.CharField(max_length=100, blank=True, null=True, verbose_name="显示名称", help_text="显示名称")
    value = models.CharField(max_length=100, blank=True, null=True, verbose_name="实际值", help_text="实际值")
    code = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name="编码", help_text="编码")
    parent = models.ForeignKey(to='CategoryDict', on_delete=models.CASCADE, default=None, verbose_name="上级",
                               db_constraint=False, null=True, blank=True, help_text="上级")

    class Meta:
        db_table = 'system_category_dict'
        verbose_name = "分类字典表"
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class OperationLog(CoreModel):
    request_username = models.CharField(max_length=50, blank=True, null=True, verbose_name="请求用户", help_text="请求用户")
    request_modular = models.CharField(max_length=64, verbose_name="请求模块", null=True, blank=True, help_text="请求模块")
    request_path = models.CharField(max_length=400, verbose_name="请求地址", null=True, blank=True, help_text="请求地址")
    request_body = models.TextField(verbose_name="请求参数", null=True, blank=True, help_text="请求参数")
    request_method = models.CharField(max_length=8, verbose_name="请求方式", null=True, blank=True, help_text="请求方式")
    request_msg = models.TextField(verbose_name="操作说明", null=True, blank=True, help_text="操作说明")
    request_ip = models.CharField(max_length=32, verbose_name="请求ip地址", null=True, blank=True, help_text="请求ip地址")
    request_browser = models.CharField(max_length=64, verbose_name="请求浏览器", null=True, blank=True, help_text="请求浏览器")
    response_code = models.CharField(max_length=32, verbose_name="响应状态码", null=True, blank=True, help_text="响应状态码")
    request_os = models.CharField(max_length=64, verbose_name="操作系统", null=True, blank=True, help_text="操作系统")
    json_result = models.TextField(verbose_name="返回信息", null=True, blank=True, help_text="返回信息")
    status = models.BooleanField(default=False, verbose_name="响应状态", help_text="响应状态")

    class Meta:
        db_table = 'system_operation_log'
        verbose_name = '操作日志'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)


def media_file_name(instance, filename):
    h = instance.md5sum
    basename, ext = os.path.splitext(filename)
    return os.path.join('files', h[0:1], h[1:2], h + ext.lower())


class File(CoreModel):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="实际名称", help_text="实际名称")
    save_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="存储名称", help_text="存储名称")
    url = models.FileField(upload_to=media_file_name)
    size = models.BigIntegerField(null=True, blank=True, verbose_name="大小", help_text="大小")
    md5sum = models.CharField(max_length=36, blank=True, verbose_name="文件md5", help_text="文件md5")

    class Meta:
        db_table = 'system_file'
        verbose_name = '文件管理'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)


class Area(CoreModel):
    name = models.CharField(max_length=100, verbose_name="名称", help_text="名称")
    code = models.CharField(max_length=20, verbose_name="地区编码", help_text="地区编码", unique=True, db_index=True)
    level = models.BigIntegerField(verbose_name="地区层级(1省份 2城市 3区县 4乡级)", help_text="地区层级(1省份 2城市 3区县 4乡级)")
    pinyin = models.CharField(max_length=255, verbose_name="拼音", help_text="拼音")
    initials = models.CharField(max_length=20, verbose_name="首字母", help_text="首字母")
    enable = models.BooleanField(default=True, verbose_name="是否启用", help_text="是否启用")
    pcode = models.ForeignKey(to='self', verbose_name='父地区编码', to_field="code", on_delete=models.CASCADE,
                              db_constraint=False, null=True, blank=True, help_text="父地区编码")

    class Meta:
        db_table = "system_area"
        verbose_name = '地区表'
        verbose_name_plural = verbose_name
        ordering = ('code',)

    def __str__(self):
        return f"{self.name}"


class ApiWhiteList(CoreModel):
    url = models.CharField(max_length=200, help_text="url地址", verbose_name="url")
    METHOD_CHOICES = (
        (0, "GET"),
        (1, "POST"),
        (2, "PUT"),
        (3, "DELETE"),
    )
    method = models.IntegerField(default=0, verbose_name="接口请求方法", null=True, blank=True, help_text="接口请求方法")
    enable_datasource = models.BooleanField(default=True, verbose_name="激活数据权限", help_text="激活数据权限", blank=True)

    class Meta:
        db_table = "system_api_white_list"
        verbose_name = '接口白名单'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)


class SystemConfig(CoreModel):
    parent = models.ForeignKey(to='self', verbose_name='父级', on_delete=models.CASCADE,
                               db_constraint=False, null=True, blank=True, help_text="父级")
    title = models.CharField(max_length=50, verbose_name="标题", help_text="标题")
    key = models.CharField(max_length=20, verbose_name="键", help_text="键")
    value = models.JSONField(max_length=100, verbose_name="值", help_text="值", null=True, blank=True)
    status = models.BooleanField(default=False, verbose_name="启用状态", help_text="启用状态")
    data_options = models.JSONField(verbose_name="数据options", help_text="数据options", null=True, blank=True)
    FORM_ITEM_TYPE_LIST = (
        (0, 'text'),
        (1, 'textarea'),
        (2, 'number'),
        (3, 'select'),
        (4, 'radio'),
        (5, 'checkbox'),
        (6, 'date'),
        (7, 'datetime'),
        (8, 'time'),
        (9, 'imgs'),
        (10, 'files'),
        (11, 'array'),
        (12, 'foreignkey'),
        (13, 'manytomany'),
    )
    form_item_type = models.IntegerField(choices=FORM_ITEM_TYPE_LIST, verbose_name="表单类型", help_text="表单类型", default=0,
                                         blank=True)
    rule = models.JSONField(null=True, blank=True, verbose_name="校验规则", help_text="校验规则")
    placeholder = models.CharField(max_length=50, null=True, blank=True, verbose_name="提示信息", help_text="提示信息")
    setting = models.JSONField(null=True, blank=True, verbose_name="配置", help_text="配置")

    class Meta:
        db_table = "system_config"
        verbose_name = '系统配置表'
        verbose_name_plural = verbose_name
        ordering = ('sort',)

    def __str__(self):
        return f"{self.title}"


class LoginLog(CoreModel):
    LOGIN_TYPE_CHOICES = (
        (1, '普通登录'),
    )
    username = models.CharField(max_length=32, verbose_name="登录用户名", null=True, blank=True, help_text="登录用户名")
    ip = models.CharField(max_length=32, verbose_name="登录ip", null=True, blank=True, help_text="登录ip")
    agent = models.TextField(verbose_name="agent信息", null=True, blank=True, help_text="agent信息")
    browser = models.CharField(max_length=200, verbose_name="浏览器名", null=True, blank=True, help_text="浏览器名")
    os = models.CharField(max_length=200, verbose_name="操作系统", null=True, blank=True, help_text="操作系统")
    continent = models.CharField(max_length=50, verbose_name="州", null=True, blank=True, help_text="州")
    country = models.CharField(max_length=50, verbose_name="国家", null=True, blank=True, help_text="国家")
    province = models.CharField(max_length=50, verbose_name="省份", null=True, blank=True, help_text="省份")
    city = models.CharField(max_length=50, verbose_name="城市", null=True, blank=True, help_text="城市")
    district = models.CharField(max_length=50, verbose_name="县区", null=True, blank=True, help_text="县区")
    isp = models.CharField(max_length=50, verbose_name="运营商", null=True, blank=True, help_text="运营商")
    area_code = models.CharField(max_length=50, verbose_name="区域代码", null=True, blank=True, help_text="区域代码")
    country_english = models.CharField(max_length=50, verbose_name="英文全称", null=True, blank=True, help_text="英文全称")
    country_code = models.CharField(max_length=50, verbose_name="简称", null=True, blank=True, help_text="简称")
    longitude = models.CharField(max_length=50, verbose_name="经度", null=True, blank=True, help_text="经度")
    latitude = models.CharField(max_length=50, verbose_name="纬度", null=True, blank=True, help_text="纬度")
    login_type = models.IntegerField(default=1, choices=LOGIN_TYPE_CHOICES, verbose_name="登录类型", help_text="登录类型")

    class Meta:
        db_table = 'system_login_log'
        verbose_name = '登录日志'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)


class CaptchaStore(CoreModel):
    id = models.AutoField(primary_key=True)
    challenge = models.CharField(blank=False, max_length=32)
    response = models.CharField(blank=False, max_length=32)
    hashkey = models.CharField(blank=False, max_length=40, unique=True)
    expiration = models.DateTimeField(blank=False)

    class Meta:
        db_table = 'system_captcha'
        verbose_name = '登录日志'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)


    def save(self, *args, **kwargs):
        self.response = self.response.lower()
        if not self.expiration:
            self.expiration = timezone.now() + datetime.timedelta(
                minutes=int(captcha_settings.CAPTCHA_TIMEOUT)
            )
        if not self.hashkey:
            key_ = (
                smart_text(randrange(0, MAX_RANDOM_KEY))
                + smart_text(time.time())
                + smart_text(self.challenge, errors="ignore")
                + smart_text(self.response, errors="ignore")
            ).encode("utf8")
            self.hashkey = hashlib.sha1(key_).hexdigest()
            del key_
        super(CaptchaStore, self).save(*args, **kwargs)

    def __str__(self):
        return self.challenge

    def remove_expired(cls):
        cls.objects.filter(expiration__lte=timezone.now()).delete()

    remove_expired = classmethod(remove_expired)

    @classmethod
    def generate_key(cls, generator=None):
        challenge, response = captcha_settings.get_challenge(generator)()
        store = cls.objects.create(challenge=challenge, response=response)

        return store.hashkey

    @classmethod
    def pick(cls):
        if not captcha_settings.CAPTCHA_GET_FROM_POOL:
            return cls.generate_key()

        def fallback():
            # logger.error("Couldn't get a captcha from pool, generating")
            return cls.generate_key()

        # Pick up a random item from pool
        minimum_expiration = timezone.now() + datetime.timedelta(
            minutes=int(captcha_settings.CAPTCHA_GET_FROM_POOL_TIMEOUT)
        )
        store = (
            cls.objects.filter(expiration__gt=minimum_expiration).order_by("?").first()
        )

        return (store and store.hashkey) or fallback()

    @classmethod
    def create_pool(cls, count=1000):
        assert count > 0
        while count > 0:
            cls.generate_key()
            count -= 1
