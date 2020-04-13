from uuid import UUID

from .requesters import user_stats, news_stats, comments_stats, rssparser_stats
from .celery import app
from .exceptions import ConnectionError


TASK_KWARGS = {
    'autoretry_for': (ConnectionError,),
    'retry_kwargs': {'max_retries': 10},
    'retry_backoff': True
}

TEMPLATE = "{0}.{1}.{2}"
MODULE = "tasks"
SPACE = "stats"


def send_stats(data: dict, requester):
    data, code = requester(data)

    if code == 503:
        raise ConnectionError

    return data, code


@app.task(**TASK_KWARGS, name=TEMPLATE.format(MODULE, SPACE, "user"))
def send_user_stats(user, action, input, output):
    data = {
        'user': user,
        'action': action,
        'input': input,
        'output': output,
    }

    data, code = send_stats(data, user_stats)
    return (data, code)


@app.task(**TASK_KWARGS, name=TEMPLATE.format(MODULE, SPACE, "news"))
def send_news_stats(user, action, input, output):
    data = {
        'user': user,
        'action': action,
        'input': input,
        'output': output,
    }

    data, code = send_stats(data, news_stats)
    return data, code


@app.task(**TASK_KWARGS, name=TEMPLATE.format(MODULE, SPACE, "comment"))
def send_comment_stats(user, action, input, output):
    data = {
        'user': user,
        'action': action,
        'input': input,
        'output': output,
    }

    data, code = send_stats(data, comments_stats)
    return data, code


@app.task(**TASK_KWARGS, name=TEMPLATE.format(MODULE, SPACE, "rssparser"))
def send_rssparser_stats(user, action, input, output):
    data = {
        'user': user,
        'action': action,
        'input': input,
        'output': output,
    }

    data, code = send_stats(data, rssparser_stats)
    return data, code
