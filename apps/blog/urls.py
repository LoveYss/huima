from django.contrib import admin
from django.urls import path
from django.urls import re_path

from blog.views import BlogView, BlogListView

urlpatterns = [
    # path('', admin.site.urls),
    path('', BlogListView.as_view),
    re_path(r'^blog/$', BlogView.as_view),
]
