# Generated by Django 5.1 on 2024-09-14 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_remove_profile_social_media_links_profile_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='notifications',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='privacy_policy',
            field=models.BooleanField(default=False),
        ),
    ]