from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, SoftDesk API!"})

urlpatterns = [
    path('', hello_world),
    path('users/', include('users.urls')),
]