# Generated by Django 2.2.1 on 2019-05-29 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190529_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='language',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='type',
            new_name='level',
        ),
    ]
