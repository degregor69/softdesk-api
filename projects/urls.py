from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, add_contributor

router = DefaultRouter()
router.register(r'', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:project_id>/contributors/', add_contributor, name='add_contributor'),
]
