# Generated by Django 5.1.3 on 2024-11-06 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_image',
        ),
    ]