from django.contrib import admin
from django.urls import path
from django.urls import re_path

from blog.views import BlogView, BlogListView

app_name = '[blog]'
urlpatterns = [
    # path('', admin.site.urls),
    path('', BlogListView.as_view(), name="bloglist"),
    re_path(r'^blog/(?P<title>.*)$', BlogView.as_view(), name="blog"),
]
