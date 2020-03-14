from django.shortcuts import render

from .models import UsersToken, RSSParserToken, CommetsToken, NewsToken, StatsToken
from .serializers import UsersTokenSerializer, RSSPareserTokenSerializer, CommentsTokenSerializer, NewsTokenSerializer, StatsTokenSerializer

from rest_framework.authtoken.serializers
from rest_framework.views import APIView, Request, Response
import rest_framework.status as st

from logging import getLogger

class BaseView(APIView):
    logger = getLogger('views')
    formatter = '{method} : {url} : {content_type} : {msg}'

    def __format(self, request: Request, msg: str = None) -> str:
        return self.formatter.format(
                method = request.method,
                url = request.get_raw_uri(),
                content_type = request.content_type,
                msg = msg
            )

    def info(self, request: Request, msg: str = None) -> None:
        self.logger.info(self.__format(request, msg))

    def exception(self, request: Request, msg: str = None) -> None:
        self.logger.exception(self.__format(request, msg))

class TokenAuthenticationView(BaseView):
    token_model = None
    token_serializer = None
    permission_classes = []
    authentication_classes = []
    service = ''

    def post(self, request: Request, format: str = 'json') -> Response:
        self.info(request, f'requesting token for service {self.service}')

        serializer = self.token_serializer(data = request.data, context = {'request': request})
        serializer.is_valid()

        token = self.token_model.objects.create()

        return Response(data = {'token': token.token}, status = st.HTTP_200_OK)

class UsersAuthenticationView(TokenAuthenticationView):
    token_model = UsersToken
    token_serializer = UsersTokenSerializer

class CommentsAuthenticationView(TokenAuthenticationView):
    token_model = CommetsToken
    token_serializer = CommentsTokenSerializer

class RSSParserAuthenticationView(TokenAuthenticationView):
    token_model = RSSParserToken
    token_serializer = RSSPareserTokenSerializer

class NewsAuthenticationView(TokenAuthenticationView):
    token_model = NewsToken
    token_serializer = NewsTokenSerializer

class StatsAuthenticationView(TokenAuthenticationView):
    token_model = StatsToken
    token_serializer = StatsTokenSerializer