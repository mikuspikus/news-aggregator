from rest_framework.permissions import BasePermission
from rest_framework.views import Request, APIView

class IsAuthenticatedForMethods(BasePermission):
    SAFE_METHODS = ('POST', )

    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.method in self.SAFE_METHODS or request.auth:
            return True
            
        return False