from django.db import models
from users.models import User
from projects.models import Project


class Contributor(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_contributions")
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name="project_contributors")


class Meta:
    unique_together = ('user', 'project')
