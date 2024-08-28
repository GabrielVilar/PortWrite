from django.db import models
from profiles.models import User  # Adjust import if needed

class Article(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='article_covers/', blank=True, null=True)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_flagged = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

