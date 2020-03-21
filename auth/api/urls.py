from django.urls import path

from .views import UserLoginView, AuthTokenView, UsersTokenView, CommentsTokenView, RSSParserTokenView, NewsTokenView, StatsTokenView

TOKENS = 'tokens'

urlpatterns = [
    path(f'{TOKENS}/users', UsersTokenView.as_view(), name = 'users-tokens'),
    path(f'{TOKENS}/comments', CommentsTokenView.as_view(), name = 'comments-tokens'),
    path(f'{TOKENS}/rss-parser', RSSParserTokenView.as_view(), name = 'rss-parser-tokens'),
    path(f'{TOKENS}/news', NewsTokenView.as_view(), name = 'news-tokens'),
    path(f'{TOKENS}/stats', StatsTokenView.as_view(), name = 'stats-tokens'),
    path(f'{TOKENS}/auth', AuthTokenView.as_view(), name = 'auth-tokens'),

    path(f'login', UserLoginView.as_view(), name = 'user-login'),

]
