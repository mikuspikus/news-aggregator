from .tokenauthentication.authentication import GenericExpiringTokenAuthentication
from .models import AuthToken, AuthServiceToken, UsersServiceToken, CommentsServiceToken, NewsServiceToken, RSSParserServiceToken, StatsServiceToken, AuthUser

from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import Request

from django.contrib.auth import authenticate

from typing import Tuple

class AuthServiceAuthentication(GenericExpiringTokenAuthentication):
    model = AuthServiceToken

class UsersServiceAuthentication(GenericExpiringTokenAuthentication):
    model = UsersServiceToken

class CommentsServiceAuthentication(GenericExpiringTokenAuthentication):
    model = CommentsServiceToken

class NewsServiceAuthentication(GenericExpiringTokenAuthentication):
    model = NewsServiceToken

class RSSParserServiceAuthentication(GenericExpiringTokenAuthentication):
    model = RSSParserServiceToken

class StatsServiceAuthentication(GenericExpiringTokenAuthentication):
    model = StatsServiceToken

class AuthAuthentication(GenericExpiringTokenAuthentication):
    model = AuthToken

class UserCredentialsAuthentication(BasicAuthentication):
    model = AuthUser

    def authenticate(self, request: Request) -> Tuple[AuthUser, None]:
        username, password = request.data.get('username'), request.data.get('password')

        if not username or not password:
            msg = 'No credentials provided'
            raise AuthenticationFailed(msg, code = 'authentication')

        user = authenticate(username = username, password = password)

        if not user:
            msg = 'Invalid username or password'
            raise AuthenticationFailed(msg, code = 'authentication')

        return (user, None)