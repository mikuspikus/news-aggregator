from django.urls import path

from .views import NewsVoteView, SingleNewsView, MultiNewsView

urlpatterns = [
    path(f"feeds", MultiNewsView.as_view(), name="feeds"),
    path(f"feeds/<int:pk>", SingleNewsView.as_view(), name="feed"),
]
