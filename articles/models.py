from django.db import models
from profiles.models import User  
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)  
    cover_image = models.ImageField(upload_to='article_covers/', blank=True, null=True)
    cover_image_subtitle = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_flagged = models.BooleanField(default=False)
    images = models.ImageField(upload_to='article_images/', blank=True, null=True)
    image_subtitle = models.CharField(max_length=255, blank=True, null=True)
    video = models.FileField(upload_to='article_videos/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
