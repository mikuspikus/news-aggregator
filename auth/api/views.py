from django.shortcuts import render

from .models import AuthToken, UsersToken, RSSParserToken, CommentsToken, NewsToken, StatsToken
from .serializers import UsersTokenSerializer, RSSPareserTokenSerializer, CommentsTokenSerializer, NewsTokenSerializer, StatsTokenSerializer
from .authentication import AuthAuthentication, UsersAuthentication, RSSParserAuthentication, CommentsAuthentication, NewsAuthentication, StatsAuthentication, UserCredentialsAuthentication

from .tokenauthentication.permissions import IsAuthenticatedForMethods
from .tokenauthentication.views import TokenView

from .base.views import BaseView


from rest_framework.views import Request, Response
import rest_framework.status as st

class UserLoginView(BaseView):
    authentication_classes = (UserCredentialsAuthentication, )
    token_model = AuthToken

    def post(self, request: Request, format: str = 'json') -> Response:
        self.info(request, f'user \'{request.user.username}\' requested for token')

        token, created = self.token_model.objects.get_or_create(user = request.user)

        return Response(data = {'token' : token.token}, status = st.HTTP_200_OK)

class AuthTokenView(BaseView):
    authentication_classes = (AuthAuthentication, )

    def get(self, request: Request, format: str = 'json') -> Response:
        self.info(request, f'checking logged-in user token {request.auth}')

        return Response(status = st.HTTP_200_OK)

class UsersTokenView(TokenView):
    token_model = UsersToken
    token_serializer = UsersTokenSerializer
    service = 'users'
    authentication_classes = (UsersAuthentication, )

class CommentsTokenView(TokenView):
    token_model = CommentsToken
    token_serializer = CommentsTokenSerializer
    service = 'comments'
    authentication_classes = (CommentsAuthentication, )

class RSSParserTokenView(TokenView):
    token_model = RSSParserToken
    token_serializer = RSSPareserTokenSerializer
    service = 'rss-parser'
    authentication_classes = (RSSParserAuthentication, )

class NewsTokenView(TokenView):
    token_model = NewsToken
    token_serializer = NewsTokenSerializer
    service = 'news'
    authentication_classes = (NewsAuthentication, )

class StatsTokenView(TokenView):
    token_model = StatsToken
    token_serializer = StatsTokenSerializer
    service = 'stats'
    authentication_classes = (StatsAuthentication, )