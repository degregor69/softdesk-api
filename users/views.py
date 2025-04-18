from rest_framework import viewsets, status
from rest_framework.response import Response
from users.models import User
from .serializers import UserSerializer, UserCreateResponseSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save() # This line calls the create method of the serializer
            return Response(UserCreateResponseSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)