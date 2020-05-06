from remoteauth.authentication import RemoteTokenAuthentication
from .requesters import authenticate, authenticate_oauth2

class TokenAuthentication(RemoteTokenAuthentication):
    
    def auth(self, token: str):
        return authenticate(token)

class OAuth2TokenAuthentication(RemoteTokenAuthentication):

    def auth(self, token: str):
        return authenticate_oauth2(token)