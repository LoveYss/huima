from django.db import models
from datetime import datetime


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=20, verbose_name='课程名称', default='')
    need_time = models.IntegerField(default=0, verbose_name='需要时长')  # 需要时长
    synopsis = models.CharField(max_length=50, verbose_name='课程简介')  # 课程简介
    study_len = models.IntegerField(default=0, verbose_name='学习人数')  # 有多少人学习
    career_direction = models.CharField(max_length=50, verbose_name='职业方向标签', default='全部')
    classification = models.CharField(max_length=50, verbose_name='分类标签', default='全部')
    cover = models.ImageField(max_length=100, verbose_name='课程封面', null=True, upload_to='course/')  # 课程封面
    leave = models.IntegerField(null=True, default=1, verbose_name='难易程度',
                                choices=((1, '入门'), (2, '初级'), (3, '中级'), (4, '高级')))
    yin = models.IntegerField(choices=((0, '隐'), (1, '不隐')), null=True, default=0)
    create_times = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '课程表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='章节名称')
    synopsis = models.CharField(max_length=300, null=True, verbose_name='章节简介')
    cover = models.ImageField(max_length=100, verbose_name='章节封面', null=True, upload_to='course/chapter/')
    create_times = models.DateTimeField(verbose_name='创建时间', default=datetime.now)
    up_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    course_id = models.IntegerField(verbose_name='所属的课程id')

    class Meta:
        verbose_name = '章节表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name='视频名称')
    synopsis = models.CharField(max_length=300, null=True, verbose_name='视频简介')
    cover = models.ImageField(max_length=100, verbose_name='视频封面', null=True, upload_to='course/video/img/')
    need_time = models.IntegerField(verbose_name='视频时长')
    url = models.FileField(max_length=200, verbose_name='视频地址', upload_to='course/video/video/')
    create_times = models.DateTimeField(verbose_name='创建时间', default=datetime.now)
    chapter_id = models.IntegerField(verbose_name='所属章节id')

    class Meta:
        verbose_name = '视频表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
