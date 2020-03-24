from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotAuthenticated, AuthenticationFailed
import rest_framework.status as st

from typing import Tuple

from remoteauth.authentication import RemoteTokenAuthentication
from .requesters import authenticate

class TokenAuthentication(RemoteTokenAuthentication):
    authenticate = authenticate