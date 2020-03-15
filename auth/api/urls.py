from django.urls import path

from .views import UsersToken, CommentsToken, RSSParserToken, NewsToken, StatsToken

TOKENS = 'tokens'

urlpatterns = [
    path(f'{TOKENS}/users/', UsersToken.as_view(), name = 'users-tokens'),
    path(f'{TOKENS}/comments/', CommentsToken.as_view(), name = 'comments-tokens'),
    path(f'{TOKENS}/rss-parser/', RSSParserToken.as_view(), name = 'rss-parser-tokens'),
    path(f'{TOKENS}/news/', NewsToken.as_view(), name = 'news-tokens'),
    path(f'{TOKENS}/stats/', StatsToken.as_view(), name = 'stats-tokens'),

]
