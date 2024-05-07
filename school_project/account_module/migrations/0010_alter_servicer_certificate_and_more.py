# Generated by Django 5.0.4 on 2024-05-07 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0009_alter_user_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicer',
            name='certificate',
            field=models.CharField(blank=True, max_length=100, verbose_name='مدارک تحصیلی'),
        ),
        migrations.AlterField(
            model_name='servicer',
            name='description',
            field=models.CharField(blank=True, max_length=300, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='servicer',
            name='gender',
            field=models.CharField(blank=True, max_length=100, verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='servicer',
            name='is_submited',
            field=models.BooleanField(blank=True, default=False, verbose_name='تایید شده'),
        ),
        migrations.AlterField(
            model_name='servicer',
            name='type',
            field=models.CharField(blank=True, max_length=100, verbose_name='نوع خدمات رسانی'),
        ),
    ]