from .requesters import authenticate_credentials

from generic.backends import GenericRemoteAuthBackend

from django.conf import settings
ERRORS_FIELD = getattr(settings, 'ERRORS_FIELD', 'error')


class RemoteAuthBackend(GenericRemoteAuthBackend):
    ERRORS_FIELD = ERRORS_FIELD

    def authenticate_credentials(self, username, password):
        return authenticate_credentials(username, password)
