# Generated by Django 5.1 on 2024-09-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True)),
                ('content', models.TextField(verbose_name='cодержимое статьи')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/photo', verbose_name='превью')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
                'ordering': ('-created_at',),
            },
        ),
    ]
