from remoteauth.authentication import RemoteTokenAuthentication
from .requesters import authenticate

class TokenAuthentication(RemoteTokenAuthentication):
    authenticate = authenticate