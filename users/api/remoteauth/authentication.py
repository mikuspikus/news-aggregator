from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotAuthenticated, AuthenticationFailed
import rest_framework.status as st

from typing import Tuple

from ..requesters.exceptions import ConnectionError
from ..requesters.base import BaseRequester


class RemoteTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'
    requester = None

    def authenticate_credentials(self, key: str) -> Tuple[None, str]:
        try:
            data, code = self.requester.authenticate(token=key)

        if code != 200:
            msg = data.get('error', 'Invalid or expired token')
            raise AuthenticationFailed(detail=msg, code='authentication')

        return (None, key)
