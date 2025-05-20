from django.db import models
from projects.models import Project
from contributors.models import Contributor

class Issue(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    TAG_CHOICES = [
        ('BUG', 'Bug'),
        ('FEATURE', 'Feature'),
        ('TASK', 'Task'),
    ]

    STATUS_CHOICES = [
        ('TO_DO', 'To do'),
        ('IN_PROGRESS', 'In Progress'),
        ('FINISHED', 'Finished'),
    ]

    title = models.CharField(max_length=128)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    tag = models.CharField(max_length=20, choices=TAG_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TO_DO')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="issues")
    created_by = models.ForeignKey(Contributor, on_delete=models.CASCADE, related_name="created_issues")
    assigned_to = models.ForeignKey(Contributor, null=True, blank=True, on_delete=models.SET_NULL, related_name="assigned_issues")



