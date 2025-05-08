from django.db import models
from users.models import User
from projects.models import Project

class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contributions")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="contributors")

    class Meta:
        unique_together = ('user', 'project')