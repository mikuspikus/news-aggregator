from django.shortcuts import render

from statshandling.views import BaseStatView

from remoteauth.permissions import IsRemoteAuthenticated

from .models import NewsStat, CommentsStat, RSSParserStat, UsersStat
from .serializers import NewsStatSerializer, CommentsStatSerializer, RSSParserStatSerializer, UsersStatsSerializer
from .authentication import TokenAuthentication


class StatView(BaseStatView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsRemoteAuthenticated,)


class UsersStatView(StatView):
    model = UsersStat
    serializer = UsersStatsSerializer
    service = 'user'


class CommentsStatsView(StatView):
    model = CommentsStat
    serializer = CommentsStatSerializer
    service = 'comments'


class RSSParserStatsView(StatView):
    model = RSSParserStat
    serializer = RSSParserStatSerializer
    service = 'rssparser'


class NewsStatsView(StatView):
    model = NewsStat
    serializer = UsersStatsSerializer
    service = 'news'
