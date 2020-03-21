from rest_framework.authentication import get_authorization_header, TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated

from typing import Tuple

from .models import Token

from datetime import timedelta, datetime
from django.utils import timezone
from django.conf import settings


def expires_in(token: Token) -> datetime:
    time_elapsed = timezone.now() - token.created
    time_left = timedelta(settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed

    return time_elapsed

def is_token_expired(token: Token) -> bool:
    return expires_in(token) < timedelta(seconds = 0)

def token_handler(token: Token) -> bool:
    is_expired = is_token_expired(token)

    if is_expired:
        token.delete()

    return is_expired

class GenericExpiringTokenAuthentication(TokenAuthentication):
    '''Expiring token authentication based on original DRF TokenAuthentication
    '''
    model = None
    keyword = 'Bearer'

    def authenticate_credentials(self, key: str):
        model = self.model

        try:
            token = model.objects.get(pk = key)

        except model.DoesNotExist:
            msg = 'Invalid token'
            raise AuthenticationFailed(msg, code = 'authentication')

        is_expired = token_handler(token)

        if is_expired:
            msg = 'Token has expired'
            raise NotAuthenticated(msg, code = 'authentication')

        return (None, token)