from django.contrib import admin
from apps.course import models

# Register your models here.
admin.site.register([
    models.Course,
    models.Chapter,
    models.Video,
])