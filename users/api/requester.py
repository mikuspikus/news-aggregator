from .requesters.base import BaseRequester
from .requesters.exceptions import ConnectionError

from requests.exceptions import RequestException

from typing import Tuple

from django.conf import settings

ERRORS_FIELD = settings.ERRORS_FIELD

class UsersRequester(BaseRequester):
    URLS = {}

    def authenticate(self, token: str) -> Tuple[dict, int]:
        try:
            response = self.get(
                url = self.URLS['authenticate'],
                headers = {'Authentication': token}
            )

        except RequestException as error:
            return self.process_error(error)

        return response.json(), response.status_code

    def send_credentials(self, credentials: dict) -> Tuple[dict, int]:
        try:
            response = self.post(
                url = self.URLS['send-credentials'],
                data = credentials,
                headers = None # add headers
            )

        except RequestException as error:
            return self.process_error(error)

        return response.json(), response.status_code

    def update_credentials(self, credentials: dict) -> Tuple[dict, int]:
        try:
            response = self.patch(
                url = self.URLS['update-credentials'],
                data = credentials,
                headers = None # add headers
            )

        except RequestException as error:
            return self.process_error(error)

        return response.json(), response.status_code
