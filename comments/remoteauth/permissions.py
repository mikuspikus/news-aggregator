from rest_framework.permissions import BasePermission
from rest_framework.views import Request, APIView


class IsRemoteAuthenticated(BasePermission):
    SAFE_METHODS = ['OPTIONS', "GET"]

    def has_permission(self, request: Request, view: APIView) -> bool:
        return request.method in self.SAFE_METHODS or bool(request.auth)