from django.shortcuts import render

# Create your views here.
from django.views import View
from blog.models import Blog, BlogComment
from django.db.models import Q


class BlogListView(View):
    def get(self, request):
        blogs = Blog.objects.all().order_by('-publish')
        # level = request.GET.get()
        # category = request.GET.get()
        return render(request, 'blog/bloglist.html', locals())


class BlogView(View):
    def get(self, request, title):
        blog = Blog.objects.get(title=title)
        comments = BlogComment.objects.filter(blog=blog.id)
        return render(request, 'blog/blog.html', locals())