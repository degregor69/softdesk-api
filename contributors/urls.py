from rest_framework_nested.routers import NestedDefaultRouter
from projects.views import ProjectViewSet
from .views import ContributorViewSet

from rest_framework.routers import DefaultRouter
root_router = DefaultRouter()
root_router.register(r'projects', ProjectViewSet, basename='project')

# Nested contributor router
project_contributor_router = NestedDefaultRouter(root_router, r'projects', lookup='project')
project_contributor_router.register(r'contributors', ContributorViewSet, basename='project-contributors')

urlpatterns = root_router.urls + project_contributor_router.urls
