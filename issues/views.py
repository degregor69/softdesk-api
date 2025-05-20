from rest_framework import viewsets, status
from rest_framework.response import Response
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

    def create(self, request, *args, **kwargs):
        project_id = request.data.get('project')
        project = get_object_or_404(Project, pk=project_id)
        contributor = Contributor.objects.filter(user=request.user, project=project).first()

        if not contributor:
            raise PermissionDenied("Vous devez être contributeur de ce projet pour créer une issue.")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=contributor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)