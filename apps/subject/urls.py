from django.contrib import admin
from django.urls import path
from django.urls import re_path
from .views import project_list, project_detail

urlpatterns = [
    # path('', admin.site.urls),
    path("", project_list, name="project_list"),
    path("project_detail", project_detail, name="project_list")
]
