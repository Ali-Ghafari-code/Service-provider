# Generated by Django 5.0.4 on 2024-05-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_request_module', '0004_service_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=200, null=True),
        ),
    ]