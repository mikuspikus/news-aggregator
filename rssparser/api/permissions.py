from generic.permissions import IsAuthenticatedForMethods, IsAuthorizedAndOwner
from rest_framework.views import Request
from .models import Feed

class IsAuthenticatedFor(IsAuthenticatedForMethods):
    SAFE_METHODS = ('GET', )

class IsAuthorizedAndFeedOwner(IsAuthorizedAndOwner):

    def is_owner(self, feed: Feed, request: Request) -> bool:
        return feed.user == request.auth.get('uuid')