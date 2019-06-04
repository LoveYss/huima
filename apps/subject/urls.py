from django.contrib import admin
from django.urls import path
from django.urls import re_path
from .views import Project_list, Project_detail

urlpatterns = [
    # path('', admin.site.urls),
    # re_path("project_list/(?P<page>)", Project_list.as_view(), name="project_list"),
    path("<page>", Project_list.as_view(), name="project_list"),
    path("project/<name>", Project_detail.as_view(), name="project_detail")
]
