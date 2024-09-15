from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    is_writer = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)
    full_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to=user_directory_path, default='default.png')
    
    biography = models.TextField(blank=True, null=True)  
    instagram = models.URLField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(max_length=255, blank=True, null=True)
    facebook = models.URLField(max_length=255, blank=True, null=True)
    youtube = models.URLField(max_length=255, blank=True, null=True)
    tiktok = models.URLField(max_length=255, blank=True, null=True)
    github = models.URLField(max_length=255, blank=True, null=True)

    notifications = models.BooleanField(default=False)
    privacy_policy = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class ReaderProfile(models.Model):
    user = models.OneToOneField('profiles.User', on_delete=models.CASCADE)
    saved_articles = models.ManyToManyField('articles.Article', related_name='saved_by_readers', blank=True)
    liked_articles = models.ManyToManyField('articles.Article', related_name='liked_by_readers', blank=True)
    
    def __str__(self):
        return f'Reader Profile of {self.user.username}'