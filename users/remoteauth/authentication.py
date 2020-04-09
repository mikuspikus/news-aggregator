from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotAuthenticated, AuthenticationFailed
import rest_framework.status as st

from typing import Tuple

from django.conf import settings
ERRORS_FIELD = getattr(settings, 'ERRORS_FIELD', 'error')

class RemoteTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'

    def auth(self, token: str):
        return None

    def authenticate_credentials(self, key: str) -> Tuple[None, str]:
        data, code = self.authenticate(token=key)

        if code != 200:
            msg = data.get(ERRORS_FIELD, 'Invalid or expired token')
            raise AuthenticationFailed(detail=msg, code='authentication')
        
        data['token'] = key
        return (None, data)
