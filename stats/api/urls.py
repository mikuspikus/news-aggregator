from django.urls import path

from .views import UsersStatView, CommentsStatsView, RSSParserStatsView, NewsStatsView

urlpatterns = [
    path(UsersStatView.service, UsersStatView.as_view(),
         name=UsersStatView.service),
    path(CommentsStatsView.service, CommentsStatsView.as_view(),
         name=CommentsStatsView.service),
    path(RSSParserStatsView.service, RSSParserStatsView.as_view(),
         name=RSSParserStatsView.service),
    path(NewsStatsView.service, NewsStatsView.as_view(),
         name=NewsStatsView.service),
]
