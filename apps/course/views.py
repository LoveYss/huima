from django.shortcuts import render
from course.models import *


# Create your views here.


def show_course(request):
    """
    课程展示页
    """
    course = Course.objects.all()
    return render(request, 'course/courseList.html', {'data': course})


def show_chapter(request, c_id):
    course = Course.objects.get(id=c_id)
    chapters = course.chapter_set.all()

    ## ['zhuanf' :{}]

    chapter = Chapter.objects.get(course_id=c_id)
    chapter_list = []
    for i in chapters:
        pass

    return render(request, 'course/chapterList.html', {'course': course, 'chapter': ''})


def show_chapter_details(request):
    return render(request, 'course/chapterDetails.html', {'data': ''})
