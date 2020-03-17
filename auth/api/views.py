from django.shortcuts import render

from .models import UsersToken, RSSParserToken, CommentsToken, NewsToken, StatsToken
from .serializers import UsersTokenSerializer, RSSPareserTokenSerializer, CommentsTokenSerializer, NewsTokenSerializer, StatsTokenSerializer
from .authentication import UsersAuthentication, RSSParserAuthentication, CommentsAuthentication, NewsAuthentication, StatsAuthentication

from .tokenauthentication.permissions import IsAuthenticatedForMethods
from .tokenauthentication.views import TokenView

from .base.views import BaseView


from rest_framework.views import Request, Response
import rest_framework.status as st

class UsersTokenView(TokenView):
    token_model = UsersToken
    token_serializer = UsersTokenSerializer
    service = 'users'
    authentication_classes = (UsersAuthentication, )

class CommentsTokenView(TokenView):
    token_model = CommentsToken
    token_serializer = CommentsTokenSerializer
    service = 'comments'
    authentication_classes = (CommentsAuthentication, )

class PostRSSParserAuthView(TokenView):
    token_model = RSSParserToken
    token_serializer = RSSPareserTokenSerializer
    service = 'rss-parser'
    authentication_classes = (RSSParserAuthentication, )

class NewsTokenView(TokenView):
    token_model = NewsToken
    token_serializer = NewsTokenSerializer
    service = 'news'
    authentication_classes = (NewsAuthentication, )

class StatsTokenView(TokenView):
    token_model = StatsToken
    token_serializer = StatsTokenSerializer
    service = 'stats'
    authentication_classes = (StatsAuthentication, )