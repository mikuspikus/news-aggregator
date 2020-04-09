from generic import base
from requests.exceptions import RequestException
from typing import Tuple

from django.conf import settings

__default_urls = {
    'authenticate': 'http://localhost:8080/v0/tokens',
    'login': 'http://localhost:8080/v0/users/login',
    'auth-token': 'http://localhost:8080/v0/tokens',
    'send-credentials': 'http://localhost:8080/v0/users',
    'update-credentials' : 'http://localhost:8080/v0/users/{uuid}'
}
URLS = getattr(settings, 'URLS', __default_urls)

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
            url=URLS['auth-token'],
            headers={'Authentication': token}
        )

    except RequestException as error:
        return base.process_errr(error)

    return response.json(), response.status_code