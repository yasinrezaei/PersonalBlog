# Generated by Django 3.0.3 on 2020-08-14 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('lastname', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('description', models.TextField(verbose_name='متن معرفی')),
                ('facebook', models.CharField(max_length=100, verbose_name='فیس بوک')),
                ('github', models.CharField(max_length=100, verbose_name='گیت هاب')),
                ('twitter', models.CharField(max_length=100, verbose_name='توئیتر')),
                ('blogname', models.CharField(max_length=100, verbose_name='نام وبلاگ')),
            ],
        ),
    ]