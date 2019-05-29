from django.shortcuts import render


# Create your views here.


def show_course(request):
    """
    课程展示页
    """
    render(request, 'course/courseList.html', {'data': ''})


def show_chapter(request):
    render(request, 'course/chapterList.html', {'data': ''})


def show_chapter_details(request):
    render(request, 'course/chapterDetails.html', {'data': ''})

