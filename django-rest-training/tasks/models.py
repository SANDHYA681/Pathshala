from django.db import models
from django.contrib.auth.models import User

def generateAttachmentPath(instance, file):
    return f'attachments/{instance.id}/{file}'

class Task(models.Model):
    class statusOptions(models.TextChoices):
        PENDING = "P", "Pending"
        IN_PROGRESS = "I", "In Progress"
        COMPLETED = "C", "Completed"
        CANCELED = "X", "Canceled"

    class priorityOptions(models.TextChoices):
        LOW = "L", "Low"
        MEDIUM = "M", "Medium"
        HIGH = "H", "High"

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ManyToManyField(User, blank=True)  # You missed User here
    start_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=1,
        choices=statusOptions.choices,
        default=statusOptions.PENDING
    )
    priority = models.CharField(
        max_length=1,
        choices=priorityOptions.choices,
        default=priorityOptions.MEDIUM
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    attachment = models.FileField(upload_to=generateAttachmentPath, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title
