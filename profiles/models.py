from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_writer = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)
    full_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.user.id}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to=user_directory_path, default='default.png')
    
    def __str__(self):
        return f'{self.user.username} Profile'

class ReaderProfile(models.Model):
    user = models.OneToOneField('profiles.User', on_delete=models.CASCADE)
    saved_articles = models.ManyToManyField('articles.Article', related_name='saved_by_readers', blank=True)
    liked_articles = models.ManyToManyField('articles.Article', related_name='liked_by_readers', blank=True)
    
    def __str__(self):
        return f'Reader Profile of {self.user.username}'
