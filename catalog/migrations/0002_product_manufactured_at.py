# Generated by Django 5.1 on 2024-09-08 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateField(blank=True, help_text='Введите дату производства продукта', null=True, verbose_name='Дата производства продукта'),
        ),
    ]
