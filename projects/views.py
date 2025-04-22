from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.models import User
from .models import Project, Contributor
from .serializers import ProjectSerializer, ContributorResponseSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save(author=request.user)

            Contributor.objects.create(user=request.user, project=project)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_contributor(request, project_id):
    user_id = request.data.get('user_id')
    project = Project.objects.get(id=project_id)

    if project.author.id != request.user.id :
        return Response({"error": "You're not the author of the project. Not allowed."}, status=status.HTTP_405_BAD_REQUEST)

    try:
        user = User.objects.get(id=user_id)
    except (User.DoesNotExist):
        return Response({"error": "User or Project not found"}, status=status.HTTP_404_NOT_FOUND)

    contributor = Contributor.objects.create(user=user, project=project)
    serializer = ContributorResponseSerializer(contributor)

    print(serializer.data)

    return Response(serializer.data, status=status.HTTP_201_CREATED)