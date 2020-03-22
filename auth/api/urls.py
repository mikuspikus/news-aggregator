from django.urls import path

from .views.servicetoservice import ServicesTokenView
from .views.user import UserView, UsersView, UserLoginView, AuthTokenView

TOKENS = "tokens"
USERS = "users"

urlpatterns = [
    path(f"{TOKENS}", ServicesTokenView.as_view(), name="tokens"),

    path(f"{USERS}", UsersView.as_view(), name="user-add"),
    path(f"{USERS}/logged-in", AuthTokenView.as_view(), name="user-logged-in"),
    path(f"{USERS}/login", UserLoginView.as_view(), name="user-login"),
    path(f"{USERS}/<uuid:uuid>", UserView.as_view(), name="user-patch"),
]
