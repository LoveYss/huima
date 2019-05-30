from django.shortcuts import render
from index.models import Banner
from course.models import Course
from subject.models import ProjectDetail
# from blog.models import Blog


def show_index(request):
    banners_img = Banner.objects.all()
    courses_info = Course.objects.all()[:6]
    subjects_info = ProjectDetail.objects.all()[:4]
    # blogs_info = Blog.objects.all()[:4]
    context = {
        'banners_img': banners_img,
        'courses_info': courses_info,
        'subjects_info': subjects_info,
        # 'blogs_info': blogs_info,
    }
    return render(request, 'index/index.html', context)
# Create your views here.
