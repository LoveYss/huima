from django.contrib import admin
from django.urls import path
from index.views import *

urlpatterns = [
    path('', show_index, name='index'),
    path('login', LoginView.as_view(), name='login')
]
