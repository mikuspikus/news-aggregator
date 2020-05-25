import generic.base as base
from generic.decorators import TokenAuthorization

from requests.exceptions import RequestException
from typing import Tuple

from django.conf import settings
from redis import StrictRedis

__default_urls = {
    'token-oauth2': 'http://localhost:8080/oauth2/token/',
    'token-revoke-oauth2': 'http://localhost:8080/oauth2/revoke_token/',
    'exchange-code-oauth2': 'http://localhost:8080/oauth2/token/',
    'authenticate-oauth2': 'http://localhost:8080/v0/oauth2/logged-in',
    'authenticate': 'http://localhost:8080/v0/users/logged-in',
    'login': 'http://localhost:8080/v0/users/login',
    'auth-token': 'http://localhost:8080/v0/tokens',

    'news': 'http://127.0.0.1:8082/v0/news',
    'users': 'http://127.0.0.1:8081/v0/users',
    'comments': 'http://127.0.0.1:8084/v0/comments',
}
URLS = getattr(settings, 'URLS', __default_urls)

ID = getattr(settings, 'APPID', 'api')
SECRET = getattr(settings, 'APPSECRET', 'api-secret')

TOKEN_LABEL = getattr(settings, 'TOKEN_LABEL', 'users-service-token')

__default_redis_conf = {
    'host': 'localhost',
    'port': 6379, 'db': 0, 'password': None, 'decode_responses': True}
REDIS_CONF = getattr(settings, 'REDIS_CONF', __default_redis_conf)
STORAGE = StrictRedis(**REDIS_CONF)

__default_oauth2_conf = {
    'CLIENT_ID': '', 'CLIENT_SECRET': ''
}
OAUTH2 = getattr(settings, 'OAUTH2', __default_oauth2_conf)
CLIENT_ID = OAUTH2['CLIENT_ID']
CLIENT_SECRET = OAUTH2['CLIENT_SECRET']
KEYWORD = 'Bearer'



def authenticate_oauth2(token: str) -> Tuple[dict, int]:
    try:
        response = base.get(
            url=URLS['authenticate-oauth2'],
            headers={'Authorization': token}
        )

    except RequestException as error:
        return base.process_errr(error)

    return response.json(), response.status_code


def __authorization_header(token: str) -> dict:
    return {'Authorization': f"{KEYWORD} {token}"}


def patch_user(token: str, useruuid: str, userdata: dict) -> Tuple[dict, int]:
    try:
        response = base.patch(
            url=f"{URLS['users']}/{useruuid}",
            data=userdata,
            headers=__authorization_header(token)
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code


def news(token: str, page: int = 1) -> Tuple[dict, int]:
    try:
        response = base.get(
            url=f"{URLS['news']}?page={page}",
            headers=__authorization_header(token)
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code


def single_news(token: str, newsuuid: str) -> Tuple[dict, int]:
    try:
        response = base.get(
            url=f"{URLS['news']}/{newsuuid}",
            headers=__authorization_header(token)
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code


def comments(token: str, newsuuid: str) -> Tuple[dict, int]:
    try:
        response = base.get(
            url=f"{URLS['comments']}?news={newsuuid}",
            headers=__authorization_header(token)

        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code


def add_news(token: str, newsdata: dict) -> Tuple[dict, int]:
    try:
        response = base.post(
            url=URLS['news'],
            data=newsdata,
            headers=__authorization_header(token)
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code


def patch_news(token: str, newsuuid: str, newsdata: dict) -> Tuple[dict, int]:
    try:
        response = base.patch(
            url=f"{URLS['news']}/{newsuuid}",
            data=newsdata,
            headers=__authorization_header(token)
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code


def add_comment(token: str, commentdata: dict) -> Tuple[dict, int]:
    try:
        response = base.post(
            url=URLS['comments'],
            data=commentdata,
            headers=__authorization_header(token)
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code


def patch_comment(token: str, commentid: int, commentdata: dict) -> Tuple[dict, int]:
    try:
        response = base.patch(
            url=f"{URLS['comments']}/{commentid}",
            data=commentdata,
            headers=__authorization_header(token)
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code


def vote_news(token: str, newsuuid: str, votedata: dict) -> Tuple[dict, int]:
    try:
        response = base.post(
            url=f"{URLS['news']}/{newsuuid}/vote",
            data=votedata,
            headers=__authorization_header(token)
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code

def revoke_toke_oauth2(token: str) -> Tuple[dict, int]:
    data = {
        'token': token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }

    try:
        response = base.postf(
            url=URLS['token-revoke-oauth2'],
            data=data
        )

    except RequestException as error:
        return base.process_error(error)

    # empty response is exptected behavior
    return response.json() if response.text else {}, response.status_code

def refresh_token_oauth2(token: str) -> Tuple[dict, int]:
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'refresh_token',
        'refresh_token': token
    }

    try:
        response = base.postf(
            url=URLS['exchange-code-oauth2'],
            data=data
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code


def exchange_code_oauth2(code: str) -> Tuple[dict, int]:
    # possible error bacause base.post uses 'json' not 'data' argument (content-type not xxx-form-encoded)
    # try with post(data = data)
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code
    }

    try:
        response = base.postf(
            url=URLS['exchange-code-oauth2'],
            data=data
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code


def authenticate_credentials(username: str, password: str) -> Tuple[dict, int]:
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
            headers={'Authorization': token}
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
