from django.urls import path

from .views import UserView, UsersView

urlpatterns = [
    path(f"users", UsersView.as_view(), name="users"),
    path(f"users/<uuid:pk>", UserView.as_view(), name="user"),
]
