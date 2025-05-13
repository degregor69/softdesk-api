from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Issue
from .serializers import IssueSerializer
from rest_framework.exceptions import PermissionDenied
from projects.models import Project
from contributors.models import Contributor
from django.shortcuts import get_object_or_404

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        project_id = self.request.data.get('project')
        project = get_object_or_404(Project, pk=project_id)
        contributor = Contributor.objects.filter(user=self.request.user, project=project).first()

        if not contributor:
            raise PermissionDenied("Vous devez être contributeur de ce projet pour créer une issue.")

        serializer.save(created_by=contributor)