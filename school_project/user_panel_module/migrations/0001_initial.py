# Generated by Django 5.0.2 on 2024-05-13 08:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_module', '0011_alter_user_is_servicer'),
        ('user_request_module', '0008_service_pay'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=300, verbose_name='نظر کاربر')),
                ('service', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_request_module.service')),
                ('servicer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account_module.servicer')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]