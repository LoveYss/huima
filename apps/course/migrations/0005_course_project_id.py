# Generated by Django 2.2.1 on 2019-05-31 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_auto_20190530_1144'),
        ('course', '0004_auto_20190531_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='project_id',
            field=models.ManyToManyField(to='subject.ProjectDetail', verbose_name='相关项目'),
        ),
    ]
