from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from projects.views import ProjectViewSet
from .views import IssueViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')


projects_router = NestedDefaultRouter(router, r'projects', lookup='project')
projects_router.register(r'issues', IssueViewSet, basename='project-issues')

urlpatterns = router.urls + projects_router.urls
