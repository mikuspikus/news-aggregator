from django.db import models

from .tokenauthentication.models import Token

class AuthToken(Token):
    pass

class CommentsToken(Token):
    pass

class NewsToken(Token):
    pass

class RSSParserToken(Token):
    pass

class StatsToken(Token):
    pass

class UsersToken(Token):
    pass
