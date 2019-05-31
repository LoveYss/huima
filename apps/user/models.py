# -*- coding: utf-8 -*-
from datetime import datetime
import time

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    nick_name = models.CharField(max_length=30, verbose_name='昵称', default=('慧码用户' + str(int(time.time() * 1000))))
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default/male.jpg', verbose_name='用户头像')
    uuid = models.UUIDField(null=True, blank=True, verbose_name='uuid')
    birthday = models.DateField(null=True, blank=True, verbose_name='生日')
    sex = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女'), ('secrete', '保密')),
                           default='female', verbose_name='性别')
    description = models.TextField(max_length=2048, null=True, blank=True, verbose_name='描述')
    ip_last_login = models.GenericIPAddressField(null=True, blank=True, verbose_name='最后登录IP')
    ip_joined = models.GenericIPAddressField(null=True, blank=True, verbose_name='注册IP')
    qq = models.CharField(max_length=20, null=True, blank=True, verbose_name='QQ')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号码')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name


# 邮箱验证（注册或找回）
class EmailVerifiCode(models.Model):
    code = models.CharField(max_length=6, verbose_name='邮箱验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(max_length=10, choices=(('register', '注册'), ('retrieve', '找回密码')), verbose_name='验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}({})'.format(self.code, self.email)


# 分类表
class Level(models.Model):
    type = models.CharField(max_length=50, verbose_name="级别")

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = '级别'
        verbose_name_plural = verbose_name


# 语言分类表
class Category(models.Model):
    language = models.CharField(max_length=50, verbose_name="类别")

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = '类别表'
        verbose_name_plural = verbose_name
