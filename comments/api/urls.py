from django.urls import path

from .views import CommentView, CommentsView

urlpatterns = [
    path(f"comments", CommentView.as_view(), name="comments"),
    path(f"comments/<int:id_>", CommentsView.as_view(), name="comment"),
]
