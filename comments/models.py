from django.db import models
import uuid
from contributors.models import Contributor
from issues.models import Issue


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    issue = models.ForeignKey(
        Issue, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        Contributor, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
