from rest_framework.permissions import BasePermission
from contributors.models import Contributor

class IsProjectContributor(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff or request.user.is_superuser:
            return True

        project_id = (
            view.kwargs.get('project_pk') or  # For nested routes
            view.kwargs.get('pk')             # For projects routes
        )
        if not project_id:
            return True

        return Contributor.objects.filter(
            user=request.user,
            project_id=project_id
        ).exists()
