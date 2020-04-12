from generic import base
import os
from requests.exceptions import ConnectionError
from typing import Tuple

URLS = {
    'user-stats': os.environ.get('user-stats', ''),
    'news-stats': os.environ.get('news-stats', ''),
    'comments-stats': os.environ.get('comments-stats', ''),
    'rss-parser-stats': os.environ.get('rss-parser-stats', ''),
}


def user_stats(data: dict, headers: dict) -> Tuple[dict, int]:
    try:
        response = base.post(
            url=URLS['user-stats'],
            data=data,
            headers=headers
        )

    except ConnectionError as error:
        return base.process_error(error)

    return response.json(), response.status_code


def news_stats(data: dict, headers: dict) -> Tuple[dict, int]:
    try:
        response = base.post(
            url=URLS['user-stats'],
            data=data,
            headers=headers
        )

    except ConnectionError as error:
        return base.process_error(error)

    return response.json(), response.status_code


def comments_stats(data: dict, headers: dict) -> Tuple[dict, int]:
    try:
        response = base.post(
            url=URLS['user-stats'],
            data=data,
            headers=headers
        )

    except ConnectionError as error:
        return base.process_error(error)

    return response.json(), response.status_code


def rssparser_stats(data: dict, headers: dict) -> Tuple[dict, int]:
    try:
        response = base.post(
            url=URLS['user-stats'],
            data=data,
            headers=headers
        )

    except ConnectionError as error:
        return base.process_error(error)

    return response.json(), response.status_code
