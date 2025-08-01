from django.db import models
from django.contrib.auth.models import User

def generateImagePath(instance, file):
    return f'images/{instance.user.username}/{file}'

class Project(models.Model):
    class ProjectStatus(models.TextChoices):
        PENDING = 'pending', 'Pending'
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'
        CANCELED = 'canceled', 'Canceled'

    class PriorityOptions(models.TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(User, blank=True, related_name='assigned_projects')
    status = models.CharField(max_length=20, choices=ProjectStatus.choices, default=ProjectStatus.PENDING)
    priority = models.CharField(max_length=20, choices=PriorityOptions.choices, default=PriorityOptions.MEDIUM)
    image = models.ImageField(upload_to=generateImagePath, blank=True, null=True, default='images/projects/default.png')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
