from django.db import models
from datetime import datetime
from user.models import User
from subject.models import ProjectDetail
from blog.models import Blog


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
    status = models.IntegerField(choices=((0, '下架'), (1, '上架')), null=True, default=1, verbose_name='课程当前状态')
    buy = models.IntegerField(choices=((0, '未购买'), (1, '已购买')), default=0, verbose_name='是否购买课程')
    buy_channel = models.IntegerField(choices=((1, '支付宝'), (2, '微信'), (3, '信用卡'), (4, '储蓄卡'), (5, '积分兑换')),
                                      verbose_name='购买渠道', default=1)
    create_times = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    score = models.IntegerField(verbose_name='评分', default=5)
    project_id = models.ManyToManyField(ProjectDetail, verbose_name='相关项目')

    class Meta:
        verbose_name = '课程表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='章节名称')
    synopsis = models.CharField(max_length=300, null=True, verbose_name='章节简介')
    num = models.CharField(max_length=30, default='第一章')
    course_id = models.ForeignKey('Course', verbose_name='所属的课程id', on_delete=models.DO_NOTHING, blank=True)
    knowledge = models.ImageField(verbose_name='思维导图(知识点)', null='', blank='', default='')
    blog = models.ManyToManyField(Blog, verbose_name='相关博客',blank=True)

    create_times = models.DateTimeField(verbose_name='创建时间', default=datetime.now)
    up_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    status = models.IntegerField(choices=((0, '未完成'), (1, '已完成')), default=0, verbose_name='章节完成度')

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
    video_type = models.IntegerField(((1, '项目视频'), (2, '课程视频')), blank=True, default=2)
    url = models.FileField(max_length=200, verbose_name='视频地址', upload_to='course/video/video/')
    create_times = models.DateTimeField(verbose_name='创建时间', default=datetime.now)
    chapter_id = models.ForeignKey('Chapter', verbose_name='所属章节id', on_delete=models.DO_NOTHING, blank=True)

    class Meta:
        verbose_name = '视频表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Note(models.Model):
    name = models.CharField(max_length=50, null=True)
    chapter_id = models.ForeignKey('Chapter', verbose_name='所属章节id', on_delete=models.DO_NOTHING, blank=True)
    inner = models.CharField(max_length=300, blank=True, verbose_name='笔记内容')
    status = models.IntegerField(choices=((0, '屏蔽'), (1, '展示')), default=1, verbose_name='当前状态')
    user_id = models.ForeignKey(User, verbose_name='用户id', on_delete=models.DO_NOTHING, blank=True)
    create_times = models.DateTimeField(verbose_name='创建时间', default=datetime.now)

    class Meta:
        verbose_name = '笔记表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
