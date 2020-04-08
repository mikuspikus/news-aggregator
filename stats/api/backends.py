from .requesters import authenticate
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.conf import settings
ERRORS_FIELD = getattr(settings, 'ERRORS_FIELD', 'error')


class RemoteAuthBackend(ModelBackend):
    model = User

    def authenticate(self, request, username=None, password=None, **kwargs):

        data, code = authenticate(username, password)

        if code != 200:
            msg = data.get(
                ERRORS_FIELD,
                f'[auth] service responded with code: {code}'
            )
            raise ValidationError(msg, code='authorization')

        try:
            user = self.model.objects.get(username=username)

        except self.model.DoesNotExist:
            user = self.model(username)
        
        # keep 'is_staff' field updated
        user.is_staff = bool(data['is_staff'])
        user.save()

        return user

    def get_user(self, user_id):
        try:
            return self.model.objects.get(pk=user_id)

        except self.model.DoesNotExist:
            return None
