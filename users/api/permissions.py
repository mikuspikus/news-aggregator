from rest_framework.permissions import BasePermission
from rest_framework.views import Request, APIView


class IsRemoteAuthenticated(BasePermission):

    def has_permission(self, request: Request, view: APIView) -> bool:
        return bool(request.auth)