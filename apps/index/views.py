from django.shortcuts import render
from index.models import Banner


def show_index(request):
    banners_img = Banner.objects.all()
    context = {
        'banners_img': banners_img
    }
    return render(request, 'index/index.html', context)
# Create your views here.
