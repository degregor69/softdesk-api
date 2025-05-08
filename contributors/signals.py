from django.db.models.signals import post_save
from django.dispatch import receiver
from projects.models import Project
from contributors.models import Contributor

@receiver(post_save, sender=Project)
def add_author_as_contributor(sender, instance, created, **kwargs):
    if created:
        Contributor.objects.get_or_create(user=instance.author, project=instance)
