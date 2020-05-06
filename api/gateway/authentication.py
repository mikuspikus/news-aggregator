from remoteauth.authentication import RemoteTokenAuthentication

from .requesters import authenticate_oauth2

class OAuth2TokenAuthentication(RemoteTokenAuthentication):

    def auth(self, token: str):
        return authenticate_oauth2(token)