from django.contrib import admin

from operation.models import *

# Register your models here.
admin.site.register(UserCourse)
admin.site.register(FavoriteCourse)
admin.site.register(CourseComment)
admin.site.register(UserMessage)