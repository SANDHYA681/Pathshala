from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Blog(models.Model):
    def generateImagePath(instance, filename):
        return f'blog/{instance.author.username}/images/{filename}'
    
    def generateAttachmentPath(instance, filename):
        return f'blog/{instance.author.username}/attachments/{filename}'
    
    class StatusOptions(models.TextChoices):
        ACTIVE = "Active", "Active"
        INACTIVE = "Inactive", "Inactive"
    
    title = models.CharField(max_length=50 )
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    tags = TaggableManager(blank=True)
    image = models.ImageField(blank=True, null=True , upload_to=generateImagePath, default='static/images/blog1.png')
    attachment = models.FileField(blank=True, null=True, upload_to=generateAttachmentPath)
    status = models.CharField(max_length=8, choices=StatusOptions, default=StatusOptions.INACTIVE)
    created_at = models.DateTimeField( auto_now_add=True, editable=False )
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title