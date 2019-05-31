from django.shortcuts import render
from django.http import HttpResponse
from subject.models import ProjectDetail
from django.views.generic.base import View

# Create your views here.
class Project_list(View):
    def get(self, request, page):
        """
        项目列表路由函数 处理分页 和
        :param request:
        :return:
        """

        items = ProjectDetail.objects.all()
        # return HttpResponse("ddd")
        return render(request, "subject/project_list.html", locals())

class Project_detail(View):
    def get(self, request, name):
        """
        项目列表路由函数 处理分页 和
        :param request:
        :return:
        """
        return render(request, "subject/project_detail.html", locals())
