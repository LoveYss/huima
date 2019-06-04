from django.shortcuts import render
from course.models import *
from django.http import JsonResponse
from django.http import HttpResponse
import json
from subject.models import ProjectDetail
from django.core.paginator import Paginator


# Create your views here.


def show_course(request):
    """
    课程展示页
    """
    course = Course.objects.all()
    return render(request, 'course/courseList.html', {'data': course})


def show_chapter_list(request, c_id):
    """章节列表页"""
    course = Course.objects.get(id=c_id)
    # chapters=course.chapter_set.all()
    pro = course.project_id.all()
    chapters = Chapter.objects.filter(course_id=1)
    return render(request, 'course/chapterList.html',
                  {'course': course, 'chapters': chapters, 'pro': pro, 'contacts': ''})


def chapter_ajax_page(request):
    page = 1

    page_num = 2  # 每页显示条数
    contact_list = Course.objects.all()
    chapter_count = contact_list.count()
    contact_lists = contact_list.filter(id__range=[(page * page_num + 1) - page_num, page * page_num + 1]).values('id',
                                                                                                                  'name')
    page_all = chapter_count / page_num  # 总页码
    contact_lists = list(contact_lists)
    return JsonResponse(contact_lists, content_type="application/json", safe=False)
    # return HttpResponse(contact_lists)


def show_chapter(request, c_id):
    """章节详情页"""
    chapter = Chapter.objects.filter(id=c_id)
    video = Video.objects.filter(chapter_id=c_id)
    return render(request, 'course/chapter.html', {'chapter': chapter, 'video': video})


def video_play(request, v_id):
    """视频播放页"""

    video = Video.objects.filter(id=v_id)
    return render(request, 'course/video.html', {'data': ''})
