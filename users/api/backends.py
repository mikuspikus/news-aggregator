from .requesters import authenticate_credentials
from .models import User

from generic.backends import GenericRemoteAuthBackend

from django.conf import settings
ERRORS_FIELD = getattr(settings, 'ERRORS_FIELD', 'detail')


class RemoteAuthBackend(GenericRemoteAuthBackend):
    model = User
    ERRORS_FIELD = ERRORS_FIELD

    def authenticate_credentials(self, username, password):
        return authenticate_credentials(username, password)
