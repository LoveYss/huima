# Generated by Django 2.2.1 on 2019-05-28 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_img', models.ImageField(upload_to='banner/%Y/%m')),
                ('banner_img_title', models.CharField(max_length=500, verbose_name='轮播图片名称')),
                ('banner_img_nub', models.IntegerField(verbose_name='轮播图片序号')),
                ('banner_img_url', models.CharField(blank=True, max_length=500, null=True, verbose_name='轮播图片链接')),
                ('banner_img_introduce', models.CharField(blank=True, max_length=500, null=True, verbose_name='轮播图片内容')),
            ],
        ),
    ]