from django.shortcuts import render
from django.views import View
from usercenter.models import User
from blog.models import *


# Create your views here.
class UserCenter(View):
    def get(self, request, uid):
        user = User.objects.get(id=uid)
        blog = Blog.objects.get(user_id=uid)
        return render(request, 'usercenter/usercenter.html', locals())
