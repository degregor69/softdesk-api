# contributors/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from users.models import User
from projects.models import Project
from contributors.models import Contributor
from contributors.serializers import ContributorResponseSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_contributor(request):
    user_id = request.data.get('user_id')
    project_id = request.data.get('project_id')
    project = get_object_or_404(Project, id=project_id)

    if project.author.id != request.user.id:
        return Response({"error": "Only the project author can add contributors."},
                        status=status.HTTP_403_FORBIDDEN)

    if user_id == request.user.id:
        return Response({"error": "Author is already a contributor by default."},
                        status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, id=user_id)

    contributor, created = Contributor.objects.get_or_create(user=user, project=project)
    serializer = ContributorResponseSerializer(contributor)

    return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
