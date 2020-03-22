from django.urls import path

from .views.servicetoservice import (
    AuthServiceTokenView,
    UsersServiceTokenView,
    CommentsServiceTokenView,
    RSSParserServiceTokenView,
    NewsServiceTokenView,
    StatsServiceTokenView,
)
from .views.login import UserLoginView, AuthTokenView

TOKENS = "tokens"

urlpatterns = [
    path(f"{TOKENS}/users", UsersServiceTokenView.as_view(), name="users-tokens"),
    path(
        f"{TOKENS}/comments", CommentsServiceTokenView.as_view(), name="comments-tokens"
    ),
    path(
        f"{TOKENS}/rss-parser",
        RSSParserServiceTokenView.as_view(),
        name="rss-parser-tokens",
    ),
    path(f"{TOKENS}/news", NewsServiceTokenView.as_view(), name="news-tokens"),
    path(f"{TOKENS}/stats", StatsServiceTokenView.as_view(), name="stats-tokens"),
    path(f"{TOKENS}/auth", AuthServiceTokenView.as_view(), name="auth-tokens"),
    path("logged-in", AuthTokenView.as_view(), name="user-logged-in"),
    path("login", UserLoginView.as_view(), name="user-login"),
]
