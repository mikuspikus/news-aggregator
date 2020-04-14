from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class GenericRemoteAuthBackend(ModelBackend):
    model = User
    ERRORS_FIELD = ''

    def authenticate_credentials(self, username: str, password: str) -> None:
        return None

    def authenticate(self, request, username=None, password=None, **kwargs):

        data, code = self.authenticate_credentials(username = username, password = password)

        if code != 200:
            msg = data.get(
                self.ERRORS_FIELD,
                f'[auth] service responded with code: {code}'
            )
            raise ValidationError(msg, code='authorization')

        try:
            user = self.model.objects.get(username=username)

        except self.model.DoesNotExist:
            user = self.model(username=username)
        
        # keep 'is_superuser' and 'is_staff' fields updated
        # is_superuser = True let user have access to standart admin panel editing tools
        user.is_superuser = data['is_superuser']
        # is_staff = True let user pass through admin panel login form
        user.is_staff = user.is_superuser
        user.save()

        return user

    def get_user(self, user_id):
        try:
            return self.model.objects.get(pk=user_id)

        except self.model.DoesNotExist:
            return None
