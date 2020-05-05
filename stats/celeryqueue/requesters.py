from generic import base
import os
from requests.exceptions import RequestException
from typing import Tuple

from generic.decorators import TokenAuthorization

from django.conf import settings
from redis import StrictRedis

URLS = {
    'auth-token': os.environ.get('auth-token', 'http://localhost:8083/v0/auth'),
    'user-stats': os.environ.get('user-stats', 'http://localhost:8083/v0/users'),
    'news-stats': os.environ.get('news-stats', 'http://localhost:8083/v0/news'),
    'comments-stats': os.environ.get('comments-stats', 'http://localhost:8083/v0/comments'),
    'rss-parser-stats': os.environ.get('rss-parser-stats', 'http://localhost:8083/v0/rssparser'),
}

ID = os.environ.get('APPID', 'stats')
SECRET = os.environ.get('APPSECRET', 'stats-secret')

TOKEN_LABEL = os.environ.get('TOKEN_LABEL', 'stats-service-token')

__default_redis_conf = {
    'host': 'localhost',
    'port': 6379, 'db': 0, 'password': None, 'decode_responses': True}
REDIS_CONF = os.environ.get('REDIS_CONF', __default_redis_conf)
STORAGE = StrictRedis(**REDIS_CONF)


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
def user_stats(data: dict, headers: dict) -> Tuple[dict, int]:
    try:
        response = base.post(
            url=URLS['user-stats'],
            data=data,
            headers=headers
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code

@TokenAuthorization(storage=STORAGE, new=token, id=ID, secret=SECRET, t_label=TOKEN_LABEL)
def news_stats(data: dict, headers: dict) -> Tuple[dict, int]:
    print(f"data: {data}")
    try:
        response = base.post(
            url=URLS['news-stats'],
            data=data,
            headers=headers
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code


def comments_stats(data: dict, headers: dict) -> Tuple[dict, int]:
    try:
        response = base.post(
            url=URLS['comments-stats'],
            data=data,
            headers=headers
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code


def rssparser_stats(data: dict, headers: dict) -> Tuple[dict, int]:
    try:
        response = base.post(
            url=URLS['rss-parser-stats'],
            data=data,
            headers=headers
        )

    except RequestException as error:
        return base.process_error(error)

    return response.json(), response.status_code
