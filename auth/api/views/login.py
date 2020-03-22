from django.shortcuts import render

from ..models import (
    AuthToken,
    AuthServiceToken,
    UsersServiceToken,
    RSSParserServiceToken,
    CommentsServiceToken,
    NewsServiceToken,
    StatsServiceToken,
)
from ..authentication import (
    AuthAuthentication,
    UserCredentialsAuthentication,
)

from ..tokenauthentication.permissions import IsAuthenticatedForMethods

from ..base.views import BaseView


from rest_framework.views import Request, Response
import rest_framework.status as st


class UserLoginView(BaseView):
    authentication_classes = (UserCredentialsAuthentication,)
    token_model = AuthToken

    def post(self, request: Request, format: str = "json") -> Response:
        self.info(request, f"user '{request.user.username}' requested for token")

        token, created = self.token_model.objects.get_or_create(user=request.user)

        return Response(data={"token": token.token}, status=st.HTTP_200_OK)


class AuthTokenView(BaseView):
    authentication_classes = (AuthAuthentication,)

    def get(self, request: Request, format: str = "json") -> Response:
        self.info(request, f"checking logged-in user token {request.auth}")

        return Response(status=st.HTTP_200_OK)
