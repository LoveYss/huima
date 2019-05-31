from django.contrib import admin

from user.models import *


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'nick_name', 'email', 'last_login']
    search_fields = ['username', 'nick_name', 'email']
    list_filter = ['last_login', 'date_joined']


admin.site.register(User, UserAdmin)
admin.site.register(EmailVerifiCode)
admin.site.register(Level)
admin.site.register(Category)
