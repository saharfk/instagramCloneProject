# Generated by Django 2.2.10 on 2021-05-26 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20210526_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='favorited',
        ),
    ]