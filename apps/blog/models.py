from django.db import models
from user.models import *

# Create your models here.


class Blog(models.Model):
    '''博客表'''

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="博主id")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name="分类id")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="语言id")
    title = models.CharField(max_length=256, verbose_name="标题")
    front_image = models.ImageField(upload_to="blog/%Y/%m", verbose_name="博客封面图",default='')
    content = models.TextField(verbose_name="正文")
    publish = models.DateTimeField(auto_now=True, verbose_name="发布时间")
    com_num = models.IntegerField(default=0, verbose_name="评论数")
    tag_num = models.IntegerField(default=0, verbose_name="点赞数")

    def __str__(self):
        return "%s - %s" % (self.user, self.title)

    class Meta:
        ordering = ['publish']
        verbose_name = '博客表'
        verbose_name_plural = verbose_name


class BlogComment(models.Model):
    '''博客回复表'''

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="回复博客")
    content = models.TextField(verbose_name="回复内容")
    publish = models.DateTimeField(auto_now=True, verbose_name="回复时间")
    tag_num = models.IntegerField(default=0, verbose_name="点赞数")

    def __str__(self):
        return "%s - %s" % (self.user, self.blog)

    class Meta:
        ordering = ['publish']
        verbose_name = '博客回复表'
        verbose_name_plural = verbose_name