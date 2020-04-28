from generic.permissions import IsAuthenticatedForMethods, IsAuthorizedAndOwner
from rest_framework.views import Request
from .models import News

class IsAuthenticatedFor(IsAuthenticatedForMethods):
    SAFE_METHODS = ('GET', )

class IsAuthorizedAndNewsOwner(IsAuthorizedAndOwner):

    def is_owner(self, news: News, request: Request) -> bool:
        return str(news.author) == request.auth.get('uuid')