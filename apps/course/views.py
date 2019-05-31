from django.shortcuts import render
from course.models import *


# Create your views here.


def show_course(request):
    """
    课程展示页
    """
    course = Course.objects.all()
    return render(request, 'course/courseList.html', {'data': course})


def show_chapter_list(request, c_id):
    """章节列表页"""
    course = Course.objects.filter(id=c_id)
    chapters = Chapter.objects.filter(course_id=c_id)
    return render(request, 'course/chapterList.html', {'course': course[0], 'chapters': chapters})


def show_chapter(request, c_id):
    """章节详情页"""
    chapter = Chapter.objects.filter(id=c_id)
    video = Video.objects.filter(chapter_id=c_id)
    return render(request, 'course/chapter.html', {'chapter': chapter, 'video': video})


def video_play(request, v_id):
    """视频播放页"""

    video = Video.objects.filter(id=v_id)
    return render(request, 'course/video.html', {'data': ''})
