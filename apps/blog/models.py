from django.db import models

# Create your models here.

class Blog(models.Model):
    '''
    博客表
    '''

    user_id = models.IntegerField(verbose_name="博主id")
    type_id = models.IntegerField(verbose_name="分类id")
    language_id = models.IntegerField(verbose_name="语言id")
    title = models.CharField(max_length=256, verbose_name="标题")
    content = models.TextField(verbose_name="正文")
    publish = models.DateTimeField(auto_now=True, verbose_name="发布时间")

    def __str__(self):
        return ("%d - %s") % (self.user_id, self.title)

    class Meta:
        ordering = ['publish']
        verbose_name = '博客表'
        verbose_name_plural = verbose_name

class BlogComment(models.Model):
    '''
    博客回复表
    '''

    user_id = models.IntegerField(verbose_name="用户id")
    blog_id = models.IntegerField(verbose_name="回复博客id")
    content = models.TextField(verbose_name="回复内容")
    publish = models.DateTimeField(auto_now=True, verbose_name="回复时间")

    def __str__(self):
        return ("%d - %d") % (self.user_id, self.blog_id)

    class Meta:
        ordering = ['publish']
        verbose_name = '博客回复表'
        verbose_name_plural = verbose_name