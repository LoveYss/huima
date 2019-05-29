# Generated by Django 2.2.1 on 2019-05-29 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usercenter', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usercenter.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usercenter.Category', verbose_name='语言id'),
        ),
        migrations.AddField(
            model_name='blog',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usercenter.Level', verbose_name='分类id'),
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usercenter.User', verbose_name='博主id'),
        ),
    ]