# Generated by Django 5.0.4 on 2024-05-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(default=1, max_length=100, verbose_name='نام و نام خانوادگی'),
            preserve_default=False,
        ),
    ]