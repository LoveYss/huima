from django.shortcuts import render
from django.views import View
from django import forms
from usercenter.models import User
from blog.models import *


# Create your views here.
class UserCenter(View):
    def get(self, request, uid):
        user = User.objects.get(id=uid)
        blog = Blog.objects.get(user_id=uid)
        author = User.objects.get(id=blog.user_id)
        return render(request, 'usercenter/usercenter.html', locals())


class UserInfoUpdateForm(View):
    def get(self, request):
        form_obj = UserInfoUpdate()
        return render(request, 'usercenter/usercenter.html', locals())



class UserInfoUpdate(forms.Form):
    username = forms.CharField(label='昵称')
    sex = forms.CharField(label='性别')
    email = forms.EmailField(label='邮箱')
