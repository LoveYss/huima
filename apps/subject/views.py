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
        try:
            page_num = 2
            page = int(request.GET.get("page", 1))
            # print("page", page)
            # page = 1
            items = ProjectDetail.objects.filter()

            if page > len(items):
                page = 1
            elif page <= 0:
                page = 1
            items = items[page-1: page+page_num-1]
        except ValueError:
            items = ProjectDetail.objects.filter()[0:page_num]

        return render(request, "subject/project_list.html", locals())

class Project_detail(View):
    def get(self, request, name):
        """
        项目列表路由函数 处理分页 和
        :param request:
        :return:
        """
        try:
            item = ProjectDetail.objects.get(id=name)
        except Exception as e:
            pass
        return render(request, "subject/project_detail.html", locals())
