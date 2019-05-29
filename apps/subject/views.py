from django.shortcuts import render
from django.http import HttpResponse
from subject.models import ProjectDetail

# Create your views here.
def project_list(request):
    """
    项目列表路由函数 处理分页 和
    :param request:
    :return:
    """
    items = ProjectDetail.objects.all()

    return render(request, "subject/project_list.html", locals())

def project_detail(request):
    """
    项目列表路由函数 处理分页 和
    :param request:
    :return:
    """

    return render(request, "subject/project_detail.html", locals())
