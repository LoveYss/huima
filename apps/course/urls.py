from django.contrib import admin
from django.urls import path
from django.urls import re_path
from course.views import *

urlpatterns = [
    path('', show_course, name='course'),
    path('chapter/<int:c_id>', show_chapter, name='chapter'),
    path('chapter_details/', show_chapter_details, name='chapter_details'),

]
