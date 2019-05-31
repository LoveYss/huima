from datetime import datetime

from django.db import models

from user.models import User
from course.models import Course


# Create your models here.
# 学习课程
class UserCourse(models.Model):
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='初始点击时间')
    last_time = models.DateTimeField(default=datetime.now, verbose_name='最后点击时间')
    study_time = models.TimeField(max_length=20, verbose_name='学习时长')

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name


# 收藏课程
class FavoriteCourse(models.Model):
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='收藏时间')

    class Meta:
        verbose_name = '收藏课程'
        verbose_name_plural = verbose_name


# 用户课程评论
class CourseComment(models.Model):
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.DO_NOTHING)
    comment = models.TextField(verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')

    class Meta:
        verbose_name = '用户课程评论'
        verbose_name_plural = verbose_name


# 浏览博客
# 收藏博客


# 消息分类
class MessageCategory(models.Model):
    name = models.CharField(max_length=20, verbose_name='类别名')

    class Meta:
        verbose_name = '消息分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 发送信息
class UserMessage(models.Model):
    # 发送给所有用户为0
    user = models.IntegerField(default=0, verbose_name='目标用户')
    message = models.CharField(max_length=500, verbose_name='消息内容')
    is_read = models.BooleanField(default=False, verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='消息时间')
    type = models.ForeignKey(MessageCategory, verbose_name='消息分类', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = '消息'
        verbose_name_plural = verbose_name
