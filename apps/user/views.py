import json

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from user.models import User
from blog.models import Blog
from user.forms import UserModifyForm


# Create your views here.
class UserCenter(View):
    def get(self, request):
        user = request.user
        blog = Blog.objects.get(user_id=user.id)
        author = User.objects.get(id=blog.user_id)
        return render(request, 'usercenter/usercenter.html', locals())

    def post(self, request):
        user = request.user
        user_setting_form = UserModifyForm(request.POST)
        if user_setting_form.is_valid():
            modify_nick_name = request.POST.get('nick_name', '')
            if User.objects.filter(nick_name=modify_nick_name) and modify_nick_name != user.nick_name:
                errors = {"msg": "用户昵称已经被使用"}
                return HttpResponse(json.dumps(errors), content_type="application/json")
            modify_sex = request.POST.get('sex', '')
            modify_email_name = request.POST.get('email_name', '')
            modify_domain_name = request.POST.get('domain_name', '')
            modify_birthday = request.POST.get('birthday', '')
            modify_qq = request.POST.get('qq_num', '')
            modify_description = request.POST.get('description', '')
            user.nick_name = modify_nick_name
            print(modify_nick_name)
            user.sex = modify_sex
            modify_email = ''.join([modify_email_name, '@', modify_domain_name])
            print(modify_email)
            user.email = modify_email
            user.birthday = modify_birthday
            user.qq = modify_qq
            user.description = modify_description
            user.save()
            value = {"status": "success"}
            return HttpResponse(json.dumps(value), content_type="application/json")
        else:
            errors = {"status": "fail", "msg": "信息输入有误"}
            return HttpResponse(json.dumps(errors), content_type="application/json")
