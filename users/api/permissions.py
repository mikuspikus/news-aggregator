from generic.permissions import IsAuthorizedAndOwner
from rest_framework.views import Request

from .models import User


class IsAuthorizedAndUser(IsAuthorizedAndOwner):
    def is_owner(self, user: User, request: Request) -> bool:
        return user.id == request.auth.get('uuid')
