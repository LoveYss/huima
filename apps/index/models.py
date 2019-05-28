from django.db import models


class Banner(models.Model):
    banner_img = models.ImageField(upload_to='banner/%Y/%m', null=False, blank=False)
    banner_img_title = models.CharField(max_length=500, verbose_name="轮播图片名称")
    banner_img_nub = models.IntegerField(verbose_name="轮播图片序号", unique=False)
    banner_img_url = models.CharField(max_length=500, verbose_name="轮播图片链接", null=True, blank=True)
    banner_img_introduce = models.CharField(max_length=500, verbose_name="轮播图片内容", null=True, blank=True)
# Create your models here.
