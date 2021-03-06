# Generated by Django 2.2.10 on 2021-05-26 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favorited',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='follow',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='stream',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
