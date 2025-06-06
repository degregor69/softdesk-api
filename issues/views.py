from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from projects.permissions import IsProjectContributor, IsAuthor
from .models import Issue
from .serializers import IssueSerializer
from projects.models import Project
from contributors.models import Contributor
from django.shortcuts import get_object_or_404


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor, IsAuthor]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return Issue.objects.filter(project__id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        project = get_object_or_404(Project, pk=project_id)
        contributor = Contributor.objects.get(
            user=self.request.user, project=project)
        serializer.save(created_by=contributor, project=project)
