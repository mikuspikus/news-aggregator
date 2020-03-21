from .tokenauthentication.authentication import GenericExpiringTokenAuthentication
from .models import AuthToken, UsersToken, CommentsToken, NewsToken, RSSParserToken, StatsToken, AuthUser

from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import Request

from django.contrib.auth import authenticate

from typing import Tuple

class UsersAuthentication(GenericExpiringTokenAuthentication):
    model = UsersToken

class CommentsAuthentication(GenericExpiringTokenAuthentication):
    model = CommentsToken

class NewsAuthentication(GenericExpiringTokenAuthentication):
    model = NewsToken

class RSSParserAuthentication(GenericExpiringTokenAuthentication):
    model = RSSParserToken

class StatsAuthentication(GenericExpiringTokenAuthentication):
    model = RSSParserToken

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