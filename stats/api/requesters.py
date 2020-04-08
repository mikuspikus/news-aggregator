from generic import base
from requests.exceptions import RequestException

from django.conf import settings

__default_urls = {
    'login': 'http://localhost:8080/v0/users/login',
    'auth-token': 'http://localhost:8080/v0/tokens',
    'send-credentials': 'http://localhost:8080/v0/users',
    'update-credentials' : 'http://localhost:8080/v0/users/{uuid}'
}
URLS = getattr(settings, 'URLS', __default_urls)

def authenticate(username: str, password: str):
    try:
        response = base.post(
            url=URLS['login'],
            data={'username': username, 'password': password}
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code