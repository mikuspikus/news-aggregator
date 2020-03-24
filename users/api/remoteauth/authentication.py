from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotAuthenticated, AuthenticationFailed
import rest_framework.status as st

from typing import Tuple


class RemoteTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'
    authenticate = None

    def authenticate_credentials(self, key: str) -> Tuple[None, str]:
        data, code = self.authenticate(token=key)

        if code != 200:
            msg = data.get('error', 'Invalid or expired token')
            raise AuthenticationFailed(detail=msg, code='authentication')

        return (None, key)
