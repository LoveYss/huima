from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from user.models import User
from blog.models import Blog
from user.forms import UserSettingForm


# Create your views here.
class UserCenter(View):
    def get(self, request, uid):
        user = User.objects.get(id=uid)
        blog = Blog.objects.get(user_id=uid)
        author = User.objects.get(id=blog.user_id)
        return render(request, 'usercenter/usercenter.html', locals())

    def post(self, request):
        user_setting_form = UserSettingForm(request.POST)
        if user_setting_form.is_valid():
            nick_name = request.POST.get('nike_name', '')
            sex = request.POST.get('sex', '')
            email_name = request.POST.get('email_name', '')
            domain_name = request.POST.get('domain_name', '')
            birthday = request.POST.get('birthday', '')
            qq = request.POST.get('QQ', '')
            description = request.POST.get('description', '')
            print(nick_name)
            return render(request, 'usercenter/usercenter.html', locals())
        else:
            return render(request, 'usercenter/usercenter.html', {'msg': '信息有误'})
