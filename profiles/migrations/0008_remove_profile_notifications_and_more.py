# Generated by Django 5.1 on 2024-09-15 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_profile_notifications_profile_privacy_policy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='notifications',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='privacy_policy',
        ),
    ]