# Generated by Django 3.0.3 on 2020-08-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200813_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blog.Category', verbose_name='دسته بندی'),
        ),
    ]