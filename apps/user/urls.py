#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.urls import path, re_path
from user.views import UserCenter

urlpatterns = [

    path('', UserCenter.as_view(), name='usercenter'),

]

