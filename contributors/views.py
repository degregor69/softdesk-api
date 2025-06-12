from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Contributor, Project, User
from .serializers import ContributorResponseSerializer
from projects.permissions import IsAuthor
from rest_framework import status
from rest_framework.response import Response

class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorResponseSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return Contributor.objects.filter(project__id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        user_id = self.request.data.get('user_id')
        project = get_object_or_404(Project, id=project_id)

        if user_id == self.request.user.id:
            return Response({"error": "Author is already a contributor by default."},
                            status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, id=user_id)
        contributor, created = Contributor.objects.get_or_create(
            user=user, project=project)

        serializer.instance = contributor