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
        try:
            blog = Blog.objects.get(user_id=user.id)
            blog_author = User.objects.get(id=blog.user_id)
        except Exception:
            blog = None
            author = None
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
            user.sex = modify_sex
            modify_email = ''.join([modify_email_name, '@', modify_domain_name])
            user.email = modify_email
            user.birthday = modify_birthday
            user.qq = modify_qq
            user.description = modify_description
            user.save()
            msg = '修改成功'
            return render(request, 'usercenter/usercenter.html', locals())
        else:
            msg = '信息输入有误'
            return render(request, 'usercenter/usercenter.html', locals())


class UserCenterBase(View):
    def get(self, request):
        return render(request, 'usercenter/base.html', locals())


class UserCenterCourse(View):
    def get(self, request):
        return render(request, 'usercenter/course.html', locals())


class UserCenterProject(View):
    def get(self, request):
        return render(request, 'usercenter/project.html', locals())


class UserCenterSuggestion(View):
    def get(self, request):
        return render(request, 'usercenter/suggestion.html', locals())


class UserCenterError(View):
    def get(self, request):
        return render(request, 'usercenter/error.html', locals())


class UserCenterBlog(View):
    def get(self, request):
        return render(request, 'usercenter/blog.html', locals())


class UserCenterQA(View):
    def get(self, request):
        return render(request, 'usercenter/QA.html', locals())


class UserCenterNote(View):
    def get(self, request):
        return render(request, 'usercenter/note.html', locals())


class UserCenterSetting(View):
    def get(self, request):
        user = request.user
        email_name = user.email.split('@')[0]
        domain_name = user.email.split('@')[1]
        return render(request, 'usercenter/setting.html', locals())


class ChangeAvatar(View):
    def post(self, request):
        user = request.user
        modify_avatar = request.POST.get('avatar', '')
        user.avatar = modify_avatar
        user.save()
        return render(request, 'usercenter/setting.html', locals())


class ChangeUserInfo(View):
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
            user.sex = modify_sex
            modify_email = ''.join([modify_email_name, '@', modify_domain_name])
            user.email = modify_email
            user.birthday = modify_birthday
            user.qq = modify_qq
            user.description = modify_description
            user.save()
            msg = '修改成功'
            return render(request, 'usercenter/setting.html', locals())
        else:
            msg = '信息输入有误'
            return render(request, 'usercenter/setting.html', locals())
