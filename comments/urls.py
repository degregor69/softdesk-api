from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from projects.views import ProjectViewSet
from issues.views import IssueViewSet
from .views import CommentViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

projects_router = NestedDefaultRouter(router, r'projects', lookup='project')
projects_router.register(r'issues', IssueViewSet, basename='project-issues')

issues_router = NestedDefaultRouter(projects_router, r'issues', lookup='issue')
issues_router.register(r'comments', CommentViewSet, basename='issue-comments')

urlpatterns = router.urls + projects_router.urls + issues_router.urls
