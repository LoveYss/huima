import json

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from user.models import User
from blog.models import Blog
from course.models import Course
from subject.models import ProjectDetail
from task.models import Questions, QuestionsBank
from operation.models import UserCourse, CourseComment, UserBlog, BlogComment2, UserProject, \
    UserQuestion, QuestionComment, MessageCategory, UserMessage
from user.forms import UserModifyForm


# Create your views here.
class UserCenterCourse(View):
    def get(self, request):
        user = request.user
        my_courses = UserCourse.objects.filter(user=user.id).order_by('-last_time')
        return render(request, 'usercenter/course.html', locals())


class UserCenterProject(View):
    def get(self, request):
        user = request.user
        my_projects = UserProject.objects.filter(user=user.id).order_by('-last_time')
        return render(request, 'usercenter/project.html', locals())


class UserCenterSuggestion(View):
    def get(self, request):
        return render(request, 'usercenter/suggestion.html', locals())


class UserCenterError(View):
    def get(self, request):
        user = request.user
        questions = UserQuestion.objects.filter(user=user.id).filter(is_correct=False)
        questions_bank_name_list = []
        error_dict = {}
        for question in questions:
            questions_bank_name_list.append(question.questions.its_QuestionsBank.QuestionsBank_name)
        questions_bank_name_set = set(questions_bank_name_list)
        for questions_bank_name in questions_bank_name_set:
            questions_bank = QuestionsBank.objects.get(QuestionsBank_name=questions_bank_name)
            questions_bank_id = questions_bank.id
            questions_bank_img = questions_bank.img
            error_question_per_questions_bank = questions.filter(questions__its_QuestionsBank=questions_bank_id).count()
            error_dict[questions_bank_name] = [error_question_per_questions_bank, questions_bank_img]
        print(error_dict)
        return render(request, 'usercenter/error.html', locals())


class UserCenterBlog(View):
    def get(self, request):
        user = request.user
        my_blogs = Blog.objects.filter(user=user.id)
        favorite_blogs = UserBlog.objects.filter(user=user.id).filter(is_favorite=True)
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
        birthday_year = user.birthday.year
        birthday_month = user.birthday.month
        birthday_day = user.birthday.day
        birthday = '%s-%s-%s' % (str(birthday_year).zfill(4), str(birthday_month).zfill(2), str(birthday_day).zfill(2))
        return render(request, 'usercenter/setting.html', locals())

    def post(self, request):
        user = request.user
        email_name = user.email.split('@')[0]
        domain_name = user.email.split('@')[1]
        birthday_year = user.birthday.year
        birthday_month = user.birthday.month
        birthday_day = user.birthday.day
        birthday = '%s-%s-%s' % (str(birthday_year).zfill(4), str(birthday_month).zfill(2), str(birthday_day).zfill(2))
        user_setting_form = UserModifyForm(request.POST)
        if user_setting_form.is_valid():
            modify_nick_name = request.POST.get('nick_name', '')
            if User.objects.filter(nick_name=modify_nick_name) and modify_nick_name != user.nick_name:
                msg = '用户昵称已经被使用'
                return render(request, 'usercenter/setting.html', locals())
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


class ChangeAvatar(View):
    def post(self, request):
        user = request.user
        modify_img = request.FILES.get('avatar')
        import os
        from huima.settings import BASE_DIR
        avatar_path = os.path.join(BASE_DIR, 'media', 'avatar', str(user.id))
        try:
            os.makedirs(avatar_path)
        except FileExistsError as e:
            pass
        f = open(os.path.join(avatar_path, modify_img.name), 'wb')
        for chunk in modify_img.chunks():
            f.write(chunk)
        f.close()
        user.avatar = os.path.join(avatar_path, modify_img.name)
        user.save()
        msg = '修改头像成功'
        return render(request, 'usercenter/setting.html', locals())


class ChangeUserInfo(View):
    pass
