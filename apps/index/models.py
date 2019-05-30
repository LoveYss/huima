from django.db import models
from datetime import datetime


class Banner(models.Model):
    banner_img = models.ImageField(upload_to='banner/%Y/%m', null=False, blank=False)
    banner_img_title = models.CharField(max_length=500, verbose_name="轮播图片名称")
    banner_img_nub = models.IntegerField(verbose_name="轮播图片序号", unique=False)
    banner_img_url = models.CharField(max_length=500, verbose_name="轮播图片链接", null=True, blank=True)
    banner_img_introduce = models.CharField(max_length=500, verbose_name="轮播图片内容", null=True, blank=True)
# Create your models here.


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(verbose_name=u"验证码类型",
                                 choices=(("register", u"注册"), ("forget", u"找回密码"), ("update_email", u"修改邮箱")),
                                 max_length=30)
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)
