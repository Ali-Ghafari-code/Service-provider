# Generated by Django 5.0.4 on 2024-05-06 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0005_alter_user_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicer',
            old_name='experince',
            new_name='experience',
        ),
    ]
