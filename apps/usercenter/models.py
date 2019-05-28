# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.
class User(AbstractUser):
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    uuid = models.IntegerField(verbose_name='uuid', null=True, blank=True)
    sex = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女'), ('secrete', '保密')),
                           default='female', verbose_name='性别')
    description = models.TextField(max_length=2048, verbose_name='描述', null=True, blank=True)
    ip_last_login = models.CharField(max_length=128, verbose_name='最后登录IP', null=True, blank=True)
    ip_joined = models.CharField(max_length=128, verbose_name='注册IP', null=True, blank=True)
    date_last_login = models.DateField(default=datetime.now, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default/male.jpg', verbose_name='用户头像')
    qq = models.IntegerField(verbose_name='QQ', null=True, blank=True)


    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username + '\t最后登录：' + str(self.last_login)
