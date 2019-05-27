# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # uuid = models.IntegerField(max_length=11, verbose_name='uuid')
    sex = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女'), ('secrete', '保密')),
                           default='female', verbose_name='性别')

    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default/male.jpg', verbose_name='用户头像')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username + '\t最后登录：' + str(self.last_login)