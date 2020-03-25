from django.urls import path

from .views import NewsVoteView, SingleNewsView, MultiNewsView

urlpatterns = [
    path(f"news", MultiNewsView.as_view(), name="multi-news"),
    path(f"news/<uuid:pk>", SingleNewsView.as_view(), name="single-news"),
    path(f"news/<uuid:pk>/vote", NewsVoteView.as_view(), name="news-vote"),
]
