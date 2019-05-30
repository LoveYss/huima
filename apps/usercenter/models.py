# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
import time


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
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name


class Level(models.Model):
    '''
    分类表
    '''
    type = models.CharField(max_length=50, verbose_name="级别")

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = '分类表'
        verbose_name_plural = verbose_name


class Category(models.Model):
    '''
    编程语言表
    '''
    language = models.CharField(max_length=50, verbose_name="类别")

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = '编程语言表'
        verbose_name_plural = verbose_name
