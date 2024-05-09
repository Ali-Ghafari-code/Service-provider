# Generated by Django 5.0.4 on 2024-05-09 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0011_alter_user_is_servicer'),
        ('user_request_module', '0002_service_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='address',
        ),
        migrations.AlterField(
            model_name='service',
            name='gender',
            field=models.CharField(blank=True, max_length=100, verbose_name='جنسیت خدمات دهنده'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='هزینه'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_date',
            field=models.CharField(max_length=100, verbose_name='تاریخ انجام پروژه'),
        ),
        migrations.AlterField(
            model_name='service',
            name='servicer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account_module.servicer'),
        ),
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(max_length=500, verbose_name='نوع خدمات'),
        ),
    ]