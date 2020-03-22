from django.shortcuts import render

from ..models import (
    AuthToken,
    AuthServiceToken,
    UsersServiceToken,
    RSSParserServiceToken,
    CommentsServiceToken,
    NewsServiceToken,
    StatsServiceToken,
)
from ..serializers import (
    AuthServiceTokenSerializer,
    UsersServiceTokenSerializer,
    RSSPareserServiceTokenSerializer,
    CommentsServiceTokenSerializer,
    NewsTokenServiceSerializer,
    StatsTokenServiceSerializer,
)
from ..authentication import (
    AuthAuthentication,
    AuthServiceAuthentication,
    UsersServiceAuthentication,
    RSSParserServiceAuthentication,
    CommentsServiceAuthentication,
    NewsServiceAuthentication,
    StatsServiceAuthentication,
    UserCredentialsAuthentication,
)

from ..tokenauthentication.permissions import IsAuthenticatedForMethods
from ..tokenauthentication.views import TokenView

from ..base.views import BaseView


from rest_framework.views import Request, Response
import rest_framework.status as st


class AuthServiceTokenView(TokenView):
    token_model = AuthServiceToken
    token_serializer = AuthServiceTokenSerializer
    service = "auth"
    authentication_classes = (AuthServiceAuthentication,)


class UsersServiceTokenView(TokenView):
    token_model = UsersServiceToken
    token_serializer = UsersServiceTokenSerializer
    service = "users"
    authentication_classes = (UsersServiceAuthentication,)


class CommentsServiceTokenView(TokenView):
    token_model = CommentsServiceToken
    token_serializer = CommentsServiceTokenSerializer
    service = "comments"
    authentication_classes = (CommentsServiceAuthentication,)


class RSSParserServiceTokenView(TokenView):
    token_model = RSSParserServiceToken
    token_serializer = RSSPareserServiceTokenSerializer
    service = "rss-parser"
    authentication_classes = (RSSParserServiceAuthentication,)


class NewsServiceTokenView(TokenView):
    token_model = NewsServiceToken
    token_serializer = NewsTokenServiceSerializer
    service = "news"
    authentication_classes = (NewsServiceAuthentication,)


class StatsServiceTokenView(TokenView):
    token_model = StatsServiceToken
    token_serializer = StatsTokenServiceSerializer
    service = "stats"
    authentication_classes = (StatsServiceAuthentication,)

