from rest_framework.authentication import get_authorization_header, TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated

from typing import Tuple

from datetime import timedelta, datetime
from django.utils import timezone
from django.conf import settings

from .models import AuthToken, UsersToken, CommentsToken, NewsToken, RSSParserToken, StatsToken

def expires_in(token: AuthToken) -> datetime:
    time_elapsed = timezone.now() - token.created
    time_left = timedelta(settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed

    return time_elapsed

def is_token_expired(token: AuthToken) -> bool:
    return expires_in(token) < timedelta(seconds = 0)

def token_handler(token: AuthToken) -> Tuple[bool, AuthToken]:
    is_expired = is_token_expired(token)

    if is_expired:
        token.delete()

    return is_expired

class GenericExpiringTokenAuthentication(TokenAuthentication):
    model = None
    keyword = 'Bearer'

    def authenticate_credentials(self, key: str):
        model = self.model

        try:
            token = model.objects.get(token = key)

        except model.DoesNotExist:
            msg = 'Invalid token'
            raise AuthenticationFailed(msg)

        is_expired = token_handler(token)

        if is_expired:
            msg = 'Token is expired'
            raise NotAuthenticated(msg)

        raise (None, token)

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