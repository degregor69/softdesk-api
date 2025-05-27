from rest_framework import viewsets

from contributors.models import Contributor
from .models import Comment
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(issue_id=self.kwargs['issue_pk'])

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        contributor = Contributor.objects.get(user=self.request.user, project_id=project_id)
        serializer.save(
            issue_id=self.kwargs['issue_pk'],
            author=contributor
        )