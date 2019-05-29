from django.contrib import admin
from django.urls import path
from index.views import *
from django.urls import re_path

urlpatterns = [
    path('', show_index, name='index'),
]
