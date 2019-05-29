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
    chapter = Chapter.objects.get(course_id=c_id)
    return render(request, 'course/chapterList.html', {'course': course, 'chapter': chapter})


def show_chapter_details(request):
    return render(request, 'course/chapterDetails.html', {'data': ''})
