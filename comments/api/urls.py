from django.urls import path

from .views import CommentView, CommentsView

urlpatterns = [
    path(f"comments", CommentsView.as_view(), name="comments"),
    path(f"comments/<int:id_>", CommentView.as_view(), name="comment"),
]
