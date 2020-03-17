from .tokenauthentication.authentication import GenericExpiringTokenAuthentication
from .models import AuthToken, UsersToken, CommentsToken, NewsToken, RSSParserToken, StatsToken

class UsersAuthentication(GenericExpiringTokenAuthentication):
    model = UsersToken

class CommentsAuthentication(GenericExpiringTokenAuthentication):
    model = CommentsToken

class NewsAuthentication(GenericExpiringTokenAuthentication):
    model = NewsToken

class RSSParserAuthentication(GenericExpiringTokenAuthentication):
    model = RSSParserToken

class StatsAuthentication(GenericExpiringTokenAuthentication):
    model = RSSParserToken