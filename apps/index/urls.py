from django.contrib import admin
from django.urls import path
from index.views import *

app_name = '[index]'
urlpatterns = [
    path('', show_index, name='index1'),
    path('login', LoginView.as_view(), name='login')
]
