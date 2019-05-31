from django.contrib import admin
from django.urls import path
from django.urls import re_path
from course.views import *

urlpatterns = [
    path('', show_course, name='course'),
    path('chapter/<int:c_id>/', show_chapter, name='chapter'),
    path('course/<int:c_id>', show_chapter_list, name='chapter_list'),
    path('chapter/video/<int:v_id>/', video_play, name='chapter_video'),

]
