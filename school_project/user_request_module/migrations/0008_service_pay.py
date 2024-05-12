# Generated by Django 5.0.4 on 2024-05-12 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_module', '0001_initial'),
        ('user_request_module', '0007_remove_service_slug_service_serviceid'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='pay',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_service_payment', to='payment_module.payment'),
        ),
    ]
