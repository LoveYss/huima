from django.db import models

# Create your models here.
# 项目详细表
class ProjectDetail(models.Model):
    proj_name = models.CharField(max_length=200, verbose_name='项目名称')
    proj_desc = models.CharField(verbose_name="项目简介", max_length=1024)
    # 大项目分割为小项目所以每个小项目有完成时间和状态
    proj_start = models.CharField(max_length=1024, verbose_name='项目开始', null=True, blank=True)
    proj_start_dt = models.DateTimeField(max_length=1024, verbose_name='项目开始完成时间', null=True, blank=True)
    proj_start_status = models.IntegerField(verbose_name='项目开始状态', choices=((0, '未完成'), (1, '完成')), default=0)

    proj_introduce = models.CharField(max_length=1024, verbose_name='功能介绍')
    proj_introduce_dt = models.DateTimeField(max_length=1024, verbose_name='功能介绍完成时间', null=True, blank=True)
    proj_introduce_status = models.IntegerField(verbose_name='功能介绍状态', choices=((0, '未完成'), (1, '完成')), default=0)

    proj_baseskill = models.CharField(max_length=1024, verbose_name='基础技能', null=True, blank=True)
    proj_baseskill_dt = models.DateTimeField(max_length=1024, verbose_name='基础技能完成时间', null=True, blank=True)
    proj_baseskill_status = models.IntegerField(verbose_name='基础技能状态', choices=((0, '未完成'), (1, '完成')), default=0)

    proj_display = models.CharField(max_length=1024, verbose_name='项目展示', null=True, blank=True)
    proj_display_dt = models.DateTimeField(max_length=1024, verbose_name='项目展示完成时间', null=True, blank=True)
    proj_display_status = models.IntegerField(verbose_name='项目展示状态', choices=((0, '未完成'), (1, '完成')), default=0)

    proj_aboutread = models.CharField(max_length=1024, verbose_name='相关阅读', null=True, blank=True)   # 外键字段
    proj_aboutread_dt = models.DateTimeField(max_length=1024, verbose_name='相关阅读完成时间', null=True, blank=True)
    proj_aboutread_status = models.IntegerField(verbose_name='相关阅读状态', choices=((0, '未完成'), (1, '完成')), default=0)

    proj_download = models.CharField(max_length=1024, verbose_name='资料下载', null=True, blank=True)
    proj_download_dt = models.DateTimeField(max_length=1024, verbose_name='资料下载完成时间', null=True, blank=True)
    proj_download_status = models.IntegerField(verbose_name='资料下载状态', choices=((0, '未完成'), (1, '完成')), default=0)

    proj_video = models.URLField(max_length=1024, verbose_name='相关视频', null=True, blank=True)  # 外键字段
    proj_video_dt = models.DateTimeField(max_length=1024, verbose_name='相关视频完成时间', null=True, blank=True)
    proj_video_status = models.IntegerField(verbose_name='相关视频状态', choices=((0, '未完成'), (1, '完成')), default=0)

    proj_upload = models.CharField(max_length=1024, verbose_name='上传项目', null=True, blank=True)
    proj_upload_dt = models.DateTimeField(max_length=1024, verbose_name='上传项目完成时间', null=True, blank=True)
    proj_upload_status = models.IntegerField(verbose_name='上传项目状态', choices=((0, '未完成'), (1, '完成')), default=0)

    proj_senior = models.CharField(max_length=1024, verbose_name='进阶教程', null=True, blank=True)  # 外键字段
    proj_senior_dt = models.DateTimeField(max_length=1024, verbose_name='进阶教程完成时间', null=True, blank=True)
    proj_senior_status = models.IntegerField(verbose_name='进阶教程状态', choices=((0, '未完成'), (1, '完成')), default=0)

    proj_finish = models.CharField(max_length=1024, verbose_name='项目终点', null=True, blank=True)
    proj_finish_status = models.IntegerField(verbose_name='进阶教程状态', choices=((0, '未完成'), (1, '完成')), default=0)
    # 保存图片 用于页面样式
    proj_arrowleft = models.ImageField(verbose_name='左箭头', null=True, blank=True)
    proj_arrowright = models.ImageField(verbose_name='右箭头', null=True, blank=True)
    proj_arrowdown = models.ImageField(verbose_name='下箭头', null=True, blank=True)
    proj_arrowup = models.ImageField(verbose_name='上箭头', null=True, blank=True)

    proj_date = models.DateTimeField(verbose_name='项目完成日期', null=True, blank=True)
    proj_statu = models.IntegerField(verbose_name='项目状态', choices=((0, '未完成'), (1, '完成')), default=0)
    proj_text = models.TextField(verbose_name="留言板", null=True, blank=True)    # 保留字段
    proj_bg_img = models.ImageField(verbose_name='项目背景图', null=True, blank=True, default="media/1.jpg")
    proj_progress = models.IntegerField(verbose_name="项目进度", default=0)
    project_level = (
        (0, "初级"),
        (1, "中级"),
        (2, "高级")
    )
    # 项目列表页字段
    proj_level = models.IntegerField(verbose_name="项目难度", choices=project_level, default=0)
    proj_student = models.IntegerField(verbose_name="学习人数", default=0)
    proj_teacher = models.CharField(max_length=1024, verbose_name="指导老师", null=True, blank=True)
    proj_tag = models.CharField(max_length=1024, verbose_name="项目标签", null=True, blank=True)
    proj_howlong = models.SmallIntegerField(verbose_name="项目时长", default=1)

    class Meta:
        verbose_name = '项目详细表'
        verbose_name_plural = verbose_name
        # db_tablespace = 'proj_date'
        # get_latest_by = 'proj_date'
        # managed = True
        # order_with_respect_to = 'proj_name'


    def __str__(self):
        return self.proj_name