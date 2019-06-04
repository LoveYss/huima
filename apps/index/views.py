import json

from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from index.email_send import send_register_email
from index.models import Banner
from course.models import Course
from subject.models import ProjectDetail
from django.views.generic.base import View
from blog.models import Blog
from user.models import User
# Create your views here.


def show_index(request):
    banners_img = Banner.objects.all()
    courses_info = Course.objects.all()[:6]
    subjects_info = ProjectDetail.objects.all()[:4]
    blogs_info = Blog.objects.all()[:4]
    context = {
        'banners_img': banners_img,
        'courses_info': courses_info,
        'subjects_info': subjects_info,
        'blogs_info': blogs_info,
    }
    return render(request, 'index/index.html', context)


class LoginView(View):
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    value = {"status": "success"}
                    return HttpResponse(json.dumps(value), content_type="application/json")
                else:
                    errors = {"status": "fail", "msg": "用户没有激活"}
                    return HttpResponse(json.dumps(errors), content_type="application/json")
            else:
                errors = {"status": "fail", "msg": "用户或密码错误"}
                return HttpResponse(json.dumps(errors), content_type="application/json")
        else:
            errors = {"status": "fail", "msg": "输入不合法"}
            return HttpResponse(json.dumps(errors), content_type="application/json")


class Register(View):
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("Username", "")
            if User.objects.filter(username=user_name):
                errors = {"status": "fail", "msg": "用户已经注册"}
                return HttpResponse(json.dumps(errors), content_type="application/json")
            pass_wd = request.POST.get("Password", "")
            if len(str(pass_wd)) < 6:
                errors = {"status": "fail", "msg": "密码不能小于6位"}
                return HttpResponse(json.dumps(errors), content_type="application/json")
            nickname = request.POST.get("Nickname", "")
            if User.objects.filter(nick_name=nickname):
                errors = {"status": "fail", "msg": "用户昵称已经被使用"}
                return HttpResponse(json.dumps(errors), content_type="application/json")
            user_profile = User()
            user_profile.username = user_name
            user_profile.password = make_password(pass_wd)
            user_profile.nick_name = nickname
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.save()

            send_register_email(user_name, "register")
            value = {"status": "success"}
            return HttpResponse(json.dumps(value), content_type="application/json")
        else:
            errors = {"status": "fail", "msg": "用户信息不合法！"}
            return HttpResponse(json.dumps(errors), content_type="application/json")

    def get(self, request):
        context = {}
        return render(request, 'register.html', context)


