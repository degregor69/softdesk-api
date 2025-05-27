from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, SoftDesk API!"})


urlpatterns = [
    path('', hello_world),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('comments.urls')),
    path('contributors/', include('contributors.urls')),
]
