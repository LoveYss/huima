#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.urls import path, re_path
from user.views import UserCenter, UserInfoUpdateForm

urlpatterns = [

    path('<int:uid>/', UserCenter.as_view(), name='usercenter'),

    path('submit_userinfo_update/', UserInfoUpdateForm.as_view())

]

