from django.shortcuts import render

from statshandling.views import BaseStatView

from .models import NewsStat, CommentsStat, RSSParserStat, UsersStat
from .serializer import NewsStatSerializer, CommentsStatSerializer, RSSParserStatSerializer, UsersStatsSerializer


class UsersStatView(BaseStatView):
    model = UsersStat
    serializer = UsersStatsSerializer
    service = 'user'


class CommentsStatsView(BaseStatView):
    model = CommentsStat
    serializer = CommentsStatSerializer
    service = 'comments'


class RSSParserStatsView(BaseStatView):
    model = RSSParserStat
    serializer = RSSParserStatSerializer
    service = 'user'


class NewsStatsView(BaseStatView):
    model = NewsStat
    serializer = UsersStatsSerializer
    service = 'user'
