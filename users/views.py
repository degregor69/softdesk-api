from rest_framework import viewsets, status
from rest_framework.response import Response
from users.models import User
from .serializers import UserSerializer, UserCreateResponseSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token_data = self.generate_jwt_token(user)
            return Response({
                'user': UserCreateResponseSerializer(user).data,
                'token': token_data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        self.check_object_permissions(request, self.get_object())
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.check_object_permissions(request, self.get_object())
        user = self.get_object()
        user.delete()
        return Response(
            {"deleted_user": user.username},
            status=status.HTTP_204_NO_CONTENT
        )

    def generate_jwt_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }
