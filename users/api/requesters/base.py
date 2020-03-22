from logging import getLogger
import requests

from typing import Union, Tuple

from django.conf import settings

# remake as functions module not class

ERRORS_FIELD = settings.ERRORS_FIELD

class BaseRequester:
    logger = getLogger(name = 'requesters')
    formatter = ''

    def __format(self, msg: str) -> str:
        return self.formatter.format(
            
        )

    def info(self, msg: str) -> None:
        self.logger.info(
            self.__format(msg)
        )

    def exception(self, msg: str) -> None:
        self.logger.exception(
            self.__format(msg)
        )

    def get(self, url: str, data: dict = {}, headers: dict = {}) -> requests.Response:
        self.info(f'requesting {url} with method \'GET\'')
        return requests.get(url = url, data = data, headers = headers)

    def post(self, url: str, data: dict = {}, headers: dict = {}) -> requests.Response:
        self.info(f'requesting {url} with method \'POST\'')
        return requests.post(url = url, data = data, headers = headers)

    def delete(self, url: str, headers: dict = {}) -> requests.Response:
        self.info(f'requesting {url} with method \'DELETE\'')
        return requests.delete(url = url, headers = headers)

    def patch(self, url: str, data: dict = {}, headers: dict = {}) -> requests.Response:
        self.info(f'requesting {url} with method \'PATCH\'')
        return requests.patch(url = url, data = data, headers = headers)

    def put(self, url: str, data: dict = {}, headers: dict = {}) -> requests.Response:
        self.info(f'requesting {url} with method \'PUT\'')
        return requests.put(url = url, data = data, headers = headers)

    def authenticate(self, token: str) -> None:
        raise NotImplementedError('Requester must implement this method before usage')

    def process_error(self, error: requests.exceptions.RequestException) -> Tuple[dict, int]:
        msg = str(error)
        self.exception(msg)
        
        return ({ERRORS_FIELD : msg}, 503)