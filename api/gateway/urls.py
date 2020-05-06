from django.urls import path

from gateway.views.public import CodeExchangeView
import gateway.views.protected as protected

urlpatterns = [
    path("code-exchange", CodeExchangeView.as_view(), name="code-exchange"),

    path("user", protected.UserView.as_view(), name="user"),

    path("news", protected.MultiNewsView.as_view(), name="multi-news"),
    path("news/<uuid:newsuuid>", protected.SingleNewsView.as_view(), name="single-news"),
    path("news/<uuid:newsuuid>/vote", protected.VoteView.as_view(), name="single-news-vote"),

    path("comments", protected.CommentsView.as_view(), name="comments"),
    path("comments/<int:commentid>", protected.CommentView.as_view(), name="comment")
]
