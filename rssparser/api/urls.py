from django.urls import path

from .views import FeedView, FeedsView

urlpatterns = [
    path(f"feeds", FeedsView.as_view(), name="feeds"),
    path(f"feeds/<int:pk>", FeedView.as_view(), name="feed"),
]
