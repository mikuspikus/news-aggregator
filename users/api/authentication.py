from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotAuthenticated, AuthenticationFailed
import rest_framework.status as st

from typing import Tuple

from .requesters.users import UsersRequester
from .requesters.exceptions import ConnectionError

class RemoteTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'

    def authenticate_credentials(self, key: str) -> Tuple[None, str]:
        try:
            data, code = UsersRequester.authenticate(token = key)

        except ConnectionError as error:
            msg = str(error)
            raise AuthenticationFailed(detail = msg, code = st.HTTP_503_SERVICE_UNAVAILABLE)

        if code == 402:
            msg = 'Invalid or experied token'
            raise AuthenticationFailed(detail = msg)

        return (None, key)