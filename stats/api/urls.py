from django.urls import path

from .views import UsersStatView, CommentsStatsView, RSSParserStatsView, NewsStatsView

urlpatterns = [
    path(UsersStatView.service, UsersStatView.as_view(),
         name='stats-users'),
    path(CommentsStatsView.service, CommentsStatsView.as_view(),
         name='stats-comments'),
    path(RSSParserStatsView.service, RSSParserStatsView.as_view(),
         name='stats-rss-parser'),
    path(NewsStatsView.service, NewsStatsView.as_view(),
         name='stats-news'),
]
