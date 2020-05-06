from logging import getLogger
import requests

from typing import Union, Tuple

from django.conf import settings

import os
ERRORS_FIELD = os.environ.get('ERRORS_FIELD', 'error')
FORMATTER = os.environ.get('FORMATTER', '')

logger = getLogger(name='requesters')


def __format(msg: str) -> str:
    return FORMATTER.format()


def info(msg: str) -> None:
    logger.info(__format(msg))


def exception(msg: str) -> None:
    logger.exception(__format(msg))


def get(url: str, data: dict = {}, headers: dict = {}) -> requests.Response:
    info(f'requesting {url} with method \'GET\'')
    return requests.get(url=url, json=data, headers=headers)


def postf(url: str, data: dict = {}, headers: dict = {}) -> requests.Response:
    info(f'requesting {url} with method \'POST\'')
    return requests.post(url=url, data=data, headers=headers)

def post(url: str, data: dict = {}, headers: dict = {}) -> requests.Response:
    info(f'requesting {url} with method \'POST\'')
    return requests.post(url=url, json=data, headers=headers)


def delete(url: str, headers: dict = {}) -> requests.Response:
    info(f'requesting {url} with method \'DELETE\'')
    return requests.delete(url=url, headers=headers)


def patch(url: str, data: dict = {}, headers: dict = {}) -> requests.Response:
    info(f'requesting {url} with method \'PATCH\'')
    return requests.patch(url=url, json=data, headers=headers)


def put(url: str, data: dict = {}, headers: dict = {}) -> requests.Response:
    info(f'requesting {url} with method \'PUT\'')
    return requests.put(url=url, json=data, headers=headers)


def process_error(error: requests.exceptions.RequestException) -> Tuple[dict, int]:
    msg = str(error)
    exception(msg)

    return ({ERRORS_FIELD: 'Connection to [auth] service failed'}, 503)
