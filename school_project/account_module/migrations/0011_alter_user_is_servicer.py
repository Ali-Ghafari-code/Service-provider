# Generated by Django 5.0.4 on 2024-05-08 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0010_alter_servicer_certificate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_servicer',
            field=models.BooleanField(default=False, verbose_name='خدمات دهنده'),
        ),
    ]
