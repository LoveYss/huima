#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.urls import path, re_path
from user.views import *

app_name = '[usercenter]'

urlpatterns = [
    path('course/', UserCenterCourse.as_view(), name='course'),
    path('project/', UserCenterProject.as_view(), name='project'),
    path('suggestion/', UserCenterSuggestion.as_view(), name='suggestion'),
    path('error/', UserCenterError.as_view(), name='error'),
    path('blog/', UserCenterBlog.as_view(), name='blog'),
    path('qa/', UserCenterQA.as_view(), name='qa'),
    path('note/', UserCenterNote.as_view(), name='note'),

    # 个人设置
    path('setting/', UserCenterSetting.as_view(), name='setting'),
    path('change_avatar/', ChangeAvatar.as_view(), name='set_avatar'),
    path('change_user_info/', ChangeUserInfo.as_view(), name='set_user_info'),

]

