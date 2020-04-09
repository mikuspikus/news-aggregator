from remoteauth.authentication import RemoteTokenAuthentication
from .requesters import authenticate

class TokenAuthentication(RemoteTokenAuthentication):
    
    def auth(self, token: str):
        return authenticate(token)