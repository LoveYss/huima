#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.urls import path, re_path
from usercenter.views import UserCenter, UserInfoUpdateForm

urlpatterns = [

    path('<int:uid>/', UserCenter.as_view(), name='个人中心'),

    path('submit_userinfo_update/', UserInfoUpdateForm.as_view())

]

