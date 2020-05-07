from django.urls import path

from .views import FeedView, FeedsView, FeedParseView # , FeedsParseView

urlpatterns = [
    path(f"feeds", FeedsView.as_view(), name="feeds"),
    path(f"feeds/<int:pk>", FeedView.as_view(), name="feed"),
    # path(f"feeds/<uuid:user>", FeedsParseView.as_view(), name="user-feeds-parse"),
    path(f"feeds/<int:pk>/parse", FeedParseView.as_view(), name="feed-parse"),
]
