from django.shortcuts import render
from .models import

def show_task(request):
    banners_img = Banner.objects.all()
    courses_info = Course.objects.all()[:6]
    subjects_info = ProjectDetail.objects.all()[:4]
    blogs_info = Blog.objects.all()[:4]
    context = {
        'banners_img': banners_img,
        'courses_info': courses_info,
        'subjects_info': subjects_info,
        'blogs_info': blogs_info,
    }
    return render(request, 'index/index.html', context)
# Create your views here.
