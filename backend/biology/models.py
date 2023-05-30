from django.db import models

# Create your models here.
from django.db import models
from utils.models import CoreModel
from django.utils import timezone


class AutoIncrementFields(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.id)


# 动物中心
class Animal(CoreModel):
    cn = models.CharField(null=False, max_length=256, verbose_name="中文名称", help_text="中文名称", blank=True)
    en = models.CharField(null=True, max_length=256, verbose_name="英文名称", help_text="英文名称", blank=True)
    ladin = models.CharField(null=True, max_length=256, verbose_name="拉丁名称", help_text="拉丁名称", blank=True)
    name_man = models.CharField(null=True, max_length=256, verbose_name="命名者", help_text="命名者", blank=True)
    name_date = models.CharField(null=True, max_length=256, verbose_name="命名时代", help_text="命名时代", blank=True)
    other_name = models.CharField(null=True, max_length=256, verbose_name="别称", help_text="别称", blank=True)
    is_protected = models.BooleanField(null=True, verbose_name="是否保护", help_text="是否保护", blank=True)
    protection_level = models.CharField(null=True, max_length=256, verbose_name="保护等级", help_text="保护等级", blank=True)
    big_class = models.CharField(null=True, max_length=256, verbose_name="大类名称", help_text="大类名称", blank=True)
    sub_class = models.CharField(null=True, max_length=256, verbose_name="小类名称", help_text="小类名称", blank=True)
    kingdom = models.CharField(null=True, max_length=256, verbose_name="界", help_text="界", blank=True)
    phylum = models.CharField(null=True, max_length=256, verbose_name="门", help_text="门", blank=True)
    subphylum = models.CharField(null=True, max_length=256, verbose_name="亚门", help_text="亚门", blank=True)
    gang = models.CharField(null=True, max_length=256, verbose_name="纲", help_text="纲", blank=True)
    subclass = models.CharField(null=True, max_length=256, verbose_name="亚纲", help_text="亚纲", blank=True)
    order = models.CharField(null=True, max_length=256, verbose_name="目", help_text="目", blank=True)
    suborder = models.CharField(null=True, max_length=256, verbose_name="亚目", help_text="亚目", blank=True)
    family = models.CharField(null=True, max_length=256, verbose_name="科", help_text="科", blank=True)
    subfamily = models.CharField(null=True, max_length=256, verbose_name="亚科", help_text="亚科", blank=True)
    species = models.CharField(null=True, max_length=256, verbose_name="种", help_text="种", blank=True)
    subspecies = models.CharField(null=True, max_length=256, verbose_name="亚种", help_text="亚种", blank=True)
    tribe = models.CharField(null=True, max_length=256, verbose_name="族", help_text="族", blank=True)
    genus = models.CharField(null=True, max_length=256, verbose_name="属", help_text="属", blank=True)
    grow = models.CharField(null=True, max_length=256, verbose_name="成长阶段", help_text="成长阶段", blank=True)
    introduction = models.CharField(null=True, max_length=2000, verbose_name="简介", help_text="简介", blank=True)
    notes = models.CharField(null=True, max_length=256, verbose_name="备注", help_text="备注", blank=True)
    url = models.CharField(max_length=255, help_text="图片", null=True, blank=True, )
    k_code = models.CharField(null=True, max_length=256, verbose_name="知识库id", help_text="知识库id", blank=True)
    k_name = models.CharField(null=True, max_length=256, verbose_name="知识库名称", help_text="知识库名称", blank=True)
    recognition_id = models.CharField(null=True, max_length=256, verbose_name="识别编号", help_text="识别编号", blank=True)

    class Meta:
        db_table = "biology_animal"
        verbose_name = '动物分类'
        verbose_name_plural = verbose_name
        # 定义排序规则
        ordering = ('-create_datetime',)


class Animal_knowledge(CoreModel):
    name = models.CharField(null=False, max_length=256, verbose_name="动物名称", help_text="动物名称", blank=True)
    description = models.TextField(verbose_name="形态特征", help_text="形态特征", null=True, blank=True, )
    habitat = models.TextField(verbose_name="栖息环境", help_text="栖息环境", null=True, blank=True, )
    live = models.TextField(verbose_name="生活习性", help_text="生活习性", blank=True, null=True)
    reproduction = models.TextField(verbose_name="繁殖方式", help_text="繁殖方式", null=True, blank=True, )
    distribution = models.TextField(verbose_name="地域分布", help_text="地域分布", null=True, blank=True, )
    subclass_distribution = models.TextField(verbose_name="亚种分布", help_text="亚种分布", null=True, blank=True, )
    family_distribution = models.TextField(verbose_name="种群现状", help_text="种群现状", null=True, blank=True, )
    protection_level = models.TextField(verbose_name="保护级别", help_text="保护级别", null=True, blank=True, )
    notes = models.TextField(verbose_name="备注", help_text="备注", null=True, blank=True, )
    animal_id = models.TextField(verbose_name="动物编号", help_text="动物编号", null=True, blank=True, )

    class Meta:
        db_table = "biology_animal_knowledge"
        verbose_name = '动物知识库'
        verbose_name_plural = verbose_name
        # 定义排序规则
        ordering = ('-create_datetime',)


class Animal_classification(CoreModel):
    name = models.CharField(null=True, max_length=256, verbose_name="动物具体类名", help_text="动物具体类名", blank=True)
    notes = models.TextField(verbose_name="备注", help_text="备注", null=True, blank=True, )
    type = models.TextField(verbose_name="分类级别", help_text="分类级别", null=False, blank=True, )
    animal_id = models.TextField(verbose_name="动物编号", help_text="动物编号", null=True, blank=True, )

    class Meta:
        db_table = "biology_animal_classification"
        verbose_name = '动物分类管理'
        verbose_name_plural = verbose_name
        # 定义排序规则
        ordering = ('-create_datetime',)


# 植物中心

class Botany(CoreModel):
    cn = models.CharField(null=False, max_length=256, verbose_name="中文名称", help_text="中文名称", blank=True)
    en = models.CharField(null=True, max_length=256, verbose_name="英文名称", help_text="英文名称", blank=True)
    ladin = models.CharField(null=True, max_length=256, verbose_name="拉丁名称", help_text="拉丁名称", blank=True)
    name_man = models.CharField(null=True, max_length=256, verbose_name="命名者", help_text="命名者", blank=True)
    name_date = models.CharField(null=True, max_length=256, verbose_name="命名时代", help_text="命名时代", blank=True)
    other_name = models.CharField(null=True, max_length=256, verbose_name="别称", help_text="别称", blank=True)
    is_protected = models.BooleanField(null=True, verbose_name="是否保护", help_text="是否保护", blank=True)
    protection_level = models.CharField(null=True, max_length=256, verbose_name="保护等级", help_text="保护等级", blank=True)
    big_class = models.CharField(null=True, max_length=256, verbose_name="大类名称", help_text="大类名称", blank=True)
    sub_class = models.CharField(null=True, max_length=256, verbose_name="小类名称", help_text="小类名称", blank=True)
    kingdom = models.CharField(null=True, max_length=256, verbose_name="界", help_text="界", blank=True)
    phylum = models.CharField(null=True, max_length=256, verbose_name="门", help_text="门", blank=True)
    subphylum = models.CharField(null=True, max_length=256, verbose_name="亚门", help_text="亚门", blank=True)
    gang = models.CharField(null=True, max_length=256, verbose_name="纲", help_text="纲", blank=True)
    subclass = models.CharField(null=True, max_length=256, verbose_name="亚纲", help_text="亚纲", blank=True)
    order = models.CharField(null=True, max_length=256, verbose_name="目", help_text="目", blank=True)
    suborder = models.CharField(null=True, max_length=256, verbose_name="亚目", help_text="亚目", blank=True)
    family = models.CharField(null=True, max_length=256, verbose_name="科", help_text="科", blank=True)
    subfamily = models.CharField(null=True, max_length=256, verbose_name="亚科", help_text="亚科", blank=True)
    species = models.CharField(null=True, max_length=256, verbose_name="种", help_text="种", blank=True)
    subspecies = models.CharField(null=True, max_length=256, verbose_name="亚种", help_text="亚种", blank=True)
    tribe = models.CharField(null=True, max_length=256, verbose_name="族", help_text="族", blank=True)
    genus = models.CharField(null=True, max_length=256, verbose_name="属", help_text="属", blank=True)
    grow = models.CharField(null=True, max_length=256, verbose_name="成长阶段", help_text="成长阶段", blank=True)
    introduction = models.CharField(null=True, max_length=2000, verbose_name="简介", help_text="简介", blank=True)
    notes = models.CharField(null=True, max_length=256, verbose_name="备注", help_text="备注", blank=True)
    url = models.CharField(max_length=255, help_text="图片", null=True, blank=True, )
    k_code = models.CharField(null=True, max_length=256, verbose_name="知识库id", help_text="知识库id", blank=True)
    k_name = models.CharField(null=True, max_length=256, verbose_name="知识库名称", help_text="知识库名称", blank=True)
    recognition_id = models.CharField(null=True, max_length=256, verbose_name="识别编号", help_text="识别编号", blank=True)

    class Meta:
        db_table = "biology_botany"
        verbose_name = '植物分类'
        verbose_name_plural = verbose_name
        # 定义排序规则
        ordering = ('-create_datetime',)


class Botany_knowledge(CoreModel):
    name = models.CharField(null=False, max_length=256, verbose_name="植物名称", help_text="植物名称", blank=True)
    description = models.TextField(verbose_name="形态特征", help_text="形态特征", null=True, blank=True, )
    habitat = models.TextField(verbose_name="栖息环境", help_text="栖息环境", null=True, blank=True, )
    live = models.TextField(verbose_name="生活习性", help_text="生活习性", blank=True, null=True)
    reproduction = models.TextField(verbose_name="繁殖方式", help_text="繁殖方式", null=True, blank=True, )
    distribution = models.TextField(verbose_name="地域分布", help_text="地域分布", null=True, blank=True, )
    subclass_distribution = models.TextField(verbose_name="亚种分布", help_text="亚种分布", null=True, blank=True, )
    family_distribution = models.TextField(verbose_name="种群现状", help_text="种群现状", null=True, blank=True, )
    protection_level = models.TextField(verbose_name="保护级别", help_text="保护级别", null=True, blank=True, )
    notes = models.TextField(verbose_name="备注", help_text="备注", null=True, blank=True, )
    botany_id = models.TextField(verbose_name="植物编号", help_text="植物编号", null=True, blank=True, )

    class Meta:
        db_table = "biology_botany_knowledge"
        verbose_name = '植物知识库'
        verbose_name_plural = verbose_name
        # 定义排序规则
        ordering = ('-create_datetime',)


class Botany_classification(CoreModel):
    name = models.CharField(null=True, max_length=256, verbose_name="植物具体类名", help_text="植物具体类名", blank=True)
    notes = models.TextField(verbose_name="备注", help_text="备注", null=True, blank=True, )
    type = models.TextField(verbose_name="分类级别", help_text="分类级别", null=False, blank=True, )
    botany_id = models.TextField(verbose_name="植物编号", help_text="植物编号", null=True, blank=True, )

    class Meta:
        db_table = "biology_botany_classification"
        verbose_name = '植物分类管理'
        verbose_name_plural = verbose_name
        # 定义排序规则
        ordering = ('-create_datetime',)


class Equipment(CoreModel):
    name = models.CharField(null=False, max_length=256, verbose_name="设备名称", help_text="设备名称", blank=True)
    model = models.CharField(null=False, max_length=256, verbose_name="设备型号", help_text="设备型号", blank=True)
    type = models.CharField(null=True, max_length=256, verbose_name="设备类型", help_text="设备类型", blank=True)
    status = models.CharField(null=True, max_length=256, verbose_name="设备状态", help_text="设备状态", blank=True)
    fps = models.CharField(null=True, max_length=256, verbose_name="拍摄帧率", help_text="拍摄帧率", blank=True)
    pixel = models.CharField(null=True, max_length=256, verbose_name="系统总像素", help_text="系统总像素", blank=True)
    resolution = models.CharField(null=True, max_length=256, verbose_name="分辨率", help_text="分辨率", blank=True)
    size = models.CharField(null=True, max_length=256, verbose_name="外观尺寸", help_text="外观尺寸", blank=True)
    start_time = models.TimeField(null=True, verbose_name="拍摄开始时间", help_text="拍摄开始时间", blank=True)
    end_time = models.TimeField(null=True, verbose_name="拍摄结束时间", help_text="拍摄结束时间", blank=True)
    interval_time = models.CharField(null=True, max_length=256, verbose_name="拍摄间隔时间", help_text="拍摄间隔时间", blank=True)
    weight = models.CharField(null=True, max_length=64, verbose_name="重量", help_text="重量", blank=True)
    input_voltage = models.CharField(null=True, max_length=64, verbose_name="输入电压", help_text="输入电压", blank=True)
    power_supply = models.CharField(null=True, max_length=64, verbose_name="电源功率", help_text="电源功率", blank=True)
    is_waterproof = models.BooleanField(null=True, verbose_name="是否防水", help_text="是否防水", blank=True)
    waterproof_grade = models.CharField(null=True, max_length=256, verbose_name="防水等级", help_text="防水等级", blank=True)
    is_dustproof = models.BooleanField(null=True, verbose_name="是否防尘", help_text="是否防尘", blank=True)
    dustproof_grade = models.CharField(null=True, max_length=256, verbose_name="防尘等级", help_text="防尘等级", blank=True)
    brand = models.CharField(null=True, max_length=256, verbose_name="设备品牌", help_text="设备品牌", blank=True)
    range = models.CharField(null=True, max_length=256, verbose_name="监控范围", help_text="监控范围", blank=True)
    is_examine = models.BooleanField(null=True, verbose_name="拍照图片是否审核", help_text="拍照图片是否审核", blank=True)
    longitude = models.FloatField(null=True, verbose_name="经度", help_text="经度", blank=True)
    latitude = models.FloatField(null=True, verbose_name="纬度", help_text="纬度", blank=True)
    is_dataShow = models.BooleanField(null=True, verbose_name="是否开启大数据展示", help_text="是否开启大数据展示", blank=True)
    equipment_id = models.CharField(null=True, max_length=64, verbose_name="云设备ID", help_text="监控范围", blank=True)
    channel_number = models.CharField(null=True, max_length=64, verbose_name="云设备通道号", help_text="云设备通道号", blank=True)
    equipment_Ip = models.CharField(null=True, max_length=64, verbose_name="摄像头Ip", help_text="摄像头Ip", blank=True)
    equipment_port = models.CharField(null=True, max_length=64, verbose_name="摄像头端口", help_text="摄像头端口", blank=True)
    equipment_count = models.CharField(null=True, max_length=64, verbose_name="摄像头账号", help_text="摄像头账号", blank=True)
    equipment_password = models.CharField(null=True, max_length=64, verbose_name="摄像头密码", help_text="摄像头密码", blank=True)
    notes = models.TextField(verbose_name="备注", help_text="备注", null=True, blank=True, )
    is_screenShow = models.BooleanField(null=True, verbose_name="是否用于大屏展示", help_text="是否用于大屏展示", blank=True)
    point_name = models.TextField(verbose_name="点位名称", help_text="点位名称", null=True, blank=True, )
    point_id = models.CharField(max_length=256, verbose_name="点位编号", help_text="点位编号", null=True, blank=True, )
    living_url = models.CharField(max_length=256, verbose_name="直播地址", help_text="直播地址", null=True, blank=True,)
    equipment_number = models.CharField(null=True, max_length=64, verbose_name="设备id", help_text="设备id", blank=True)

    class Meta:
        db_table = "biology_equipment"
        verbose_name = '设备'
        verbose_name_plural = verbose_name
        # 定义排序规则
        ordering = ('-create_datetime',)


class Recognition(CoreModel):
    name = models.CharField(null=False, max_length=256, verbose_name="名字", help_text="名字", blank=True)
    EnglishName = models.CharField(null=False, max_length=256, verbose_name="英文名", help_text="英文名", blank=True)
    type = models.CharField(max_length=32, verbose_name="识别类型", help_text="识别类型", null=True, blank=True, )
    recognition_number = models.IntegerField(verbose_name="识别数量", help_text="识别数量", null=True, blank=True, )
    result = models.BooleanField(verbose_name="识别结果", help_text="识别结果", null=True, blank=True, )
    degree = models.FloatField(verbose_name="置信度", help_text="置信度", null=True, blank=True, )
    time = models.DateField(verbose_name="识别时间", help_text="识别时间", null=True, blank=True, )
    isExcellent = models.BooleanField(verbose_name="是否优秀", help_text="是否优秀", null=True, blank=True, )
    url = models.CharField(max_length=255, verbose_name="视频", help_text="视频", null=True, blank=True, )
    place = models.CharField(max_length=32, verbose_name="地点", help_text="地点", null=True, blank=True, )
    # equipment_id = models.CharField(max_length=32, verbose_name="设备标号", help_text="设备标号", null=True, blank=True, )
    reserve = models.CharField(max_length=32, verbose_name="保护区", help_text="保护区", null=True, blank=True, )
    fileType = models.CharField(max_length=32, verbose_name="文件类型", help_text="文件类型", null=True, blank=True, )

    class Meta:
        db_table = "biology_recognition"
        verbose_name = '识别'
        verbose_name_plural = verbose_name
        # 定义排序规则
        ordering = ('-create_datetime',)


class RealTime_recognition(CoreModel):
    cn = models.CharField(null=True, max_length=256, verbose_name="名字", help_text="名字", blank=True)
    en = models.CharField(null=True, max_length=256, verbose_name="英文名", help_text="英文名", blank=True)
    type = models.CharField(max_length=32, verbose_name="动物类别", help_text="动物类别", null=True, blank=True, )
    degree = models.FloatField(verbose_name="置信度", help_text="置信度", null=True, blank=True, )
    time = models.CharField(max_length=32, verbose_name="拍摄时间", help_text="拍摄时间", null=True, blank=True, )
    isExcellent = models.BooleanField(verbose_name="是否优秀", help_text="是否优秀", null=True, blank=True, )
    isFalse = models.BooleanField(verbose_name="是否标错", help_text="是否标错", null=True, blank=True, )
    recognition_id = models.CharField(max_length=255, verbose_name="识别编号", help_text="识别编号", null=True, blank=True, )
    equipment_id = models.CharField(null=True, max_length=64, verbose_name="设备", help_text="设备", blank=True)
    equipment_name = models.CharField(null=True, max_length=64, verbose_name="设备名称", help_text="设备名称", blank=True)
    url = models.CharField(null=True, max_length=255, blank=True)
    start_time = models.DateTimeField(null=True, verbose_name="识别开始时间", help_text="识别开始时间", blank=True)
    end_time = models.DateTimeField(null=True, verbose_name="识别结束时间", help_text="识别结束时间", blank=True)
    batch = models.CharField(null=True, max_length=255, verbose_name="识别批次id", help_text="识别批次id", blank=True)
    result_text = models.TextField(null=True, verbose_name="结果集合", help_text="结果集合", blank=True)
    sfile_path = models.CharField(null=True, max_length=512, verbose_name="文件地址", help_text="文件地址", blank=True)
    ponit_name = models.CharField(null=True, max_length=255, verbose_name="点位名称", help_text="点位名称", blank=True)
    erro_msg = models.TextField(null=True, blank=True, max_length=255)
    point_id = models.CharField(null=True, max_length=64, verbose_name="点位id", help_text="点位id", blank=True)
    point_name = models.CharField(null=True, max_length=64, verbose_name="点位name", help_text="点位name", blank=True)
    area_id = models.CharField(null=True, max_length=64, verbose_name="区域id", help_text="区域id", blank=True)
    area_name = models.CharField(null=True, max_length=64, verbose_name="区域name", help_text="区域name", blank=True)

    class Meta:
        db_table = "biology_realtime_recognition"
        verbose_name = '实时识别'
        verbose_name_plural = verbose_name
        # 定义排序规则
        ordering = ('-create_datetime',)


class RealTimeRecognitionDetail(CoreModel):
    name = models.CharField(null=False, max_length=256, verbose_name="名字", help_text="名字", blank=True)
    recognition_id = models.CharField(max_length=255, verbose_name="识别编号", help_text="识别编号", null=True, blank=True, )
    recognition_number = models.IntegerField(verbose_name="识别数量", help_text="识别数量", null=True, blank=True, )
    batch_no = models.CharField(max_length=32, verbose_name="批次号", help_text="批次号", null=True, blank=True, )

    class Meta:
        db_table = "biology_realtime_recognition_detail"
        verbose_name = "实时识别明细"
        verbose_name_plural = verbose_name
        # 定义排序规则
        ordering = ('-create_datetime',)


class Recognition_batch(CoreModel):
    id = models.CharField(null=False, max_length=256, verbose_name="识别批次id", help_text="识别批次id", primary_key=True)
    number = models.IntegerField(null=False, verbose_name="数量", help_text="数量")
    start_time = models.DateTimeField(null=True, verbose_name="识别开始时间", help_text="识别开始时间", blank=True)
    end_time = models.DateTimeField(null=True, verbose_name="识别结束时间", help_text="识别结束时间", blank=True)
    isSuccess = models.BooleanField(verbose_name="是否成功", help_text="是否成功", null=True, blank=True, )

    class Meta:
        db_table = "biology_recognition_batch"
        verbose_name = '识别批次'
        verbose_name_plural = verbose_name
        # 定义排序规则
        ordering = ('-create_datetime',)


class Areas(CoreModel):
    id = models.CharField(null=False, max_length=256, verbose_name="区域id", help_text="区域id", primary_key=True)
    name = models.CharField(null=False, max_length=256, verbose_name="区域名", help_text="区域名", blank=True)
    address = models.CharField(null=True, max_length=256, verbose_name="投放地址", help_text="投放地址", blank=True)
    manager = models.CharField(null=True, max_length=128, verbose_name="点位负责人", help_text="点位负责人", blank=True)
    manager_phone = models.CharField(null=True, max_length=256, verbose_name="点位负责人联系方式", help_text="点位负责人联系方式",
                                     blank=True)
    introduction = models.TextField(verbose_name="点位简介", help_text="点位简介", null=True, blank=True, )
    notes = models.TextField(verbose_name="点位备注", help_text="点位备注", null=True, blank=True, )
    path = models.TextField(verbose_name="区域经纬度", help_text="区域经纬度", null=True, blank=True, )
    area_id = models.TextField(verbose_name="区域编号", help_text="区域编号", null=True, blank=True, )
    type = models.CharField(null=True, max_length=256, verbose_name="类型", help_text="类型", blank=True)

    class Meta:
        db_table = "biology_area"
        verbose_name = '区域'
        verbose_name_plural = verbose_name
        # 定义排序规则
        ordering = ('-create_datetime',)


class Point(CoreModel):
    id = models.CharField(null=False, max_length=256, verbose_name="点位id", help_text="点位id", primary_key=True)
    name = models.CharField(null=False, max_length=256, verbose_name="点位名称", help_text="点位名称", blank=True)
    time = models.DateTimeField(null=True, verbose_name="投放点位时间", help_text="投放点位时间", blank=True)
    longitude = models.FloatField(null=True, verbose_name="点位经度", help_text="点位经度", blank=True)
    latitude = models.FloatField(null=True, verbose_name="点位纬度", help_text="点位纬度", blank=True)
    area = models.CharField(null=True, max_length=256, verbose_name="所属区域名称", help_text="所属区域名称", blank=True)
    area_id = models.CharField(null=True, max_length=256, verbose_name="所属区域编号", help_text="所属区域编号", blank=True)
    manager = models.CharField(null=True, max_length=128, verbose_name="点位负责人", help_text="点位负责人", blank=True)
    manager_phone = models.CharField(null=True, max_length=256, verbose_name="点位负责人联系方式", help_text="点位负责人联系方式",
                                     blank=True)
    introduction = models.TextField(verbose_name="点位简介", help_text="点位简介", null=True, blank=True, )
    address = models.TextField(verbose_name="点位详细地址", help_text="点位详细地址", null=True, blank=True, )
    notes = models.TextField(verbose_name="点位备注", help_text="点位备注", null=True, blank=True, )
    point_id = models.TextField(verbose_name="点位编号", help_text="点位编号", null=True, blank=True, )

    class Meta:
        db_table = "biology_point"
        verbose_name = '区域点'
        verbose_name_plural = verbose_name
        # 定义排序规则
        ordering = ('-create_datetime',)


class EquipmentTemplate(CoreModel):
    name = models.CharField(null=False, max_length=256, verbose_name="设备名称", help_text="设备名称", blank=True)
    model = models.CharField(null=False, max_length=256, verbose_name="设备型号", help_text="设备型号", blank=True)
    type = models.CharField(null=True, max_length=256, verbose_name="设备类型", help_text="设备类型", blank=True)
    status = models.CharField(null=True, max_length=8, verbose_name="是否启用", help_text="设备状态", blank=True)
    fps = models.CharField(null=True, max_length=256, verbose_name="拍摄帧率", help_text="拍摄帧率", blank=True)
    pixel = models.CharField(null=True, max_length=256, verbose_name="系统总像素", help_text="系统总像素", blank=True)
    resolution = models.CharField(null=True, max_length=256, verbose_name="分辨率", help_text="分辨率", blank=True)
    size = models.CharField(null=True, max_length=256, verbose_name="外观尺寸", help_text="外观尺寸", blank=True)
    weight = models.CharField(null=True, max_length=64, verbose_name="重量", help_text="重量", blank=True)
    input_voltage = models.CharField(null=True, max_length=64, verbose_name="输入电压", help_text="输入电压", blank=True)
    power_supply = models.CharField(null=True, max_length=64, verbose_name="电源功率", help_text="电源功率", blank=True)
    is_waterproof = models.BooleanField(null=True, verbose_name="是否防水", help_text="是否防水", blank=True)
    waterproof_grade = models.CharField(null=True, max_length=256, verbose_name="防水等级", help_text="防水等级", blank=True)
    is_dustproof = models.BooleanField(null=True, verbose_name="是否防尘", help_text="是否防尘", blank=True)
    dustproof_grade = models.CharField(null=True, max_length=256, verbose_name="防尘等级", help_text="防尘等级", blank=True)

    class Meta:
        db_table = "biology_template"
        verbose_name = '设备'
        verbose_name_plural = verbose_name
        # 定义排序规则
        ordering = ('-create_datetime',)


class Warning(CoreModel):
    type = models.CharField(null=True, max_length=256, verbose_name="预警类型", help_text="预警类型", blank=True)
    message = models.CharField(null=True, max_length=256, verbose_name="预警信息内容", help_text="预警信息内容", blank=True)

    class Meta:
        db_table = "biology_warning"
        verbose_name = '预警信息'
        verbose_name_plural = verbose_name
        # 定义排序规则
        ordering = ('-create_datetime',)


class Title(CoreModel):
    name = models.CharField(null=True, max_length=256, verbose_name="标题名称", help_text="标题名称", blank=True)

    class Meta:
        db_table = "Title"
        verbose_name = '标题'
        verbose_name_plural = verbose_name
        # 定义排序规则
        ordering = ('-create_datetime',)
