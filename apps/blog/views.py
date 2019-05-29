from django.shortcuts import render

# Create your views here.
from django.views import View
from blog.models import Blog, BlogComment
from django.db.models import Q


class BlogListView(View):
    def get(self, request):
        blogs = Blog.objects.all().order_by('-publish')
        return render(request, 'blog/bloglist.html', locals())

    # def catalog(self, request):
    #     type = request.GET.get('type')
    #     language = request.GET.get('language')
    #     blogs = Blog.objects.filter(Q(type=type)|Q(language=language))
    #     return render(request, 'blog/bloglist.html', locals())


class BlogView(View):
    def get(self, request, title):
        title = request.GET.get("title")
        blog = Blog.objects.get(title=title)
        return render(request, 'blog/blog.html', locals())