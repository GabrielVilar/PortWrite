from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_writer = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True)  # Add this field
    
    def __str__(self):
        return self.username

class ReaderProfile(models.Model):
    user = models.OneToOneField('profiles.User', on_delete=models.CASCADE)
    saved_articles = models.ManyToManyField('articles.Article', related_name='saved_by_readers', blank=True)
    liked_articles = models.ManyToManyField('articles.Article', related_name='liked_by_readers', blank=True)
    
    def __str__(self):
        return f'Reader Profile of {self.user.username}'
