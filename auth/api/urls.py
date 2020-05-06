from django.urls import path

from .views.servicetoservice import ServicesTokenView
from .views.user import UserView, UsersView, UserLoginView, AuthTokenView
from .views.oauth2 import OAuth2TokenView

TOKENS = "tokens"
USERS = "users"
OAUTH2 = "oauth2"

urlpatterns = [
    path(f"{OAUTH2}/logged-in", OAuth2TokenView.as_view(), name="oauth2-logged-in"),
    path(f"{TOKENS}", ServicesTokenView.as_view(), name="tokens"),
    path(f"{USERS}", UsersView.as_view(), name="user-add"),
    path(f"{USERS}/logged-in", AuthTokenView.as_view(), name="user-logged-in"),
    path(f"{USERS}/login", UserLoginView.as_view(), name="user-login"),
    path(f"{USERS}/<uuid:uuid>", UserView.as_view(), name="user-patch"),
]
