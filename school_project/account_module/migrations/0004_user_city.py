# Generated by Django 5.0.4 on 2024-05-06 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0003_alter_user_is_servicer'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, default=False, max_length=100, verbose_name='استان و شهر'),
        ),
    ]
