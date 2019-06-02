# Generated by Django 2.2.1 on 2019-06-01 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('subject', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='user_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.User', verbose_name='用户id'),
        ),
        migrations.AddField(
            model_name='course',
            name='project_id',
            field=models.ManyToManyField(to='subject.ProjectDetail', verbose_name='相关项目'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='course_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.Course', verbose_name='所属的课程id'),
        ),
    ]