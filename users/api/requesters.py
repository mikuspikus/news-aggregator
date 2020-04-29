import generic.base as base
from generic.decorators import TokenAuthorization

from requests.exceptions import RequestException
from typing import Tuple

from django.conf import settings
from redis import StrictRedis

__default_urls = {
    'authenticate': 'http://localhost:8080/v0/users/logged-in',
    'login' : 'http://localhost:8080/v0/users/login',
    'auth-token': 'http://localhost:8080/v0/tokens',
    'send-credentials': 'http://localhost:8080/v0/users',
    'update-credentials': 'http://localhost:8080/v0/users/{uuid}'
}
URLS = getattr(settings, 'URLS', __default_urls)

ID = getattr(settings, 'APPID', 'users')
SECRET = getattr(settings, 'APPSECRET', 'users-secret')

TOKEN_LABEL = getattr(settings, 'TOKEN_LABEL', 'users-service-token')

__default_redis_conf = {
    'host': 'localhost',
    'port': 6379, 'db': 0, 'password': None, 'decode_responses': True}
REDIS_CONF = getattr(settings, 'REDIS_CONF', __default_redis_conf)
STORAGE = StrictRedis(**REDIS_CONF)


def authenticate_credentials(username: str, password: str):
    try:
        response = base.post(
            url=URLS['login'],
            data={'username': username, 'password': password}
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code


def authenticate(token: str) -> Tuple[dict, int]:
    try:
        response = base.get(
            url=URLS['authenticate'],
            headers={'Authentication': token}
        )

    except RequestException as error:
        return base.process_errr(error)

    return response.json(), response.status_code

def token(id: str, secret: str) -> Tuple[dict, int]:
    try:
        response = base.post(
            url=URLS['auth-token'],
            data={'id': id, 'secret': secret}
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code


@TokenAuthorization(storage=STORAGE, new=token, id=ID, secret=SECRET, t_label=TOKEN_LABEL)
def send_credentials(credentials: dict, headers: dict = {}) -> Tuple[dict, int]:
    try:
        response = base.post(
            url=URLS['send-credentials'],
            data=credentials,
            headers=headers
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code


@TokenAuthorization(storage=STORAGE, new=token, id=ID, secret=SECRET, t_label=TOKEN_LABEL)
def update_credentials(uuid: str, credentials: dict, headers: dict = {}) -> Tuple[dict, int]:
    try:
        response = base.patch(
            url=URLS['update-credentials'].format(uuid=uuid),
            data=credentials,
            headers=headers
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code
