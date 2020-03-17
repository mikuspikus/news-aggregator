from .requesters.base import BaseRequester
from .requesters.exceptions import ConnectionError

from requests.exceptions import RequestException

from typing import Tuple

class UsersRequester(BaseRequester):
    URLS = {}

    @staticmethod
    def authenticate(self, token: str) -> Tuple[dict, int]:
        try:
            response = self.get(
                url = self.URLS['auth'],
                headers = {'Authentication': token}
            )

        except RequestException as error:
            msg = str(error)
            self.exception(msg)
            raise ConnectionError(msg)

        return response.json(), response.status_code
