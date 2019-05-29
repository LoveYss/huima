#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.urls import path, re_path
from usercenter.views import UserCenter

urlpatterns = [

    path('<int:uid>/', UserCenter.as_view()),

]

