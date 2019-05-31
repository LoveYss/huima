from django.contrib import admin
from course import models

# Register your models here.
admin.site.register([
    models.Course,
    models.Chapter,
    models.Video,
])