from rest_framework.permissions import BasePermission
from rest_framework.views import Request, APIView

class IsAuthorized(BasePermission):
    SAFE_METHODS = ("OPTIONS", )

    def has_permission(self, request: Request, view: APIView) -> bool:
        return request.method in self.SAFE_METHODS or request.auth

class IsAuthenticatedForMethods(BasePermission):
    SAFE_METHODS = ('POST', )

    def has_permission(self, request: Request, view: APIView) -> bool:
        return request.method in self.SAFE_METHODS or request.auth

class IsAuthorizedAndOwner(BasePermission):
    SAFE_METHODS = ('GET',)

    def is_owner(self, obj, request: Request) -> bool:
        # return obj.author == user_uuid
        return True

    def has_object_permission(self, request: Request, view: APIView, obj) -> bool:
        if request.method in self.SAFE_METHODS:
            return True

        return request.auth and self.is_owner(obj, request)