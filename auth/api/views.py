from django.shortcuts import render

from .models import UsersToken, RSSParserToken, CommentsToken, NewsToken, StatsToken
from .serializers import UsersTokenSerializer, RSSPareserTokenSerializer, CommentsTokenSerializer, NewsTokenSerializer, StatsTokenSerializer
from .authentication import UsersAuthentication, RSSParserAuthentication, CommentsAuthentication, NewsAuthentication, StatsAuthentication
from .permissions import IsAuthenticatedFor

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

class TokenView(BaseView):
    token_model = None
    token_serializer = None
    permission_classes = (IsAuthenticatedFor, )
    authentication_classes = []
    service = ''

    def get(self, request: Request, format: str = 'json') -> Response:
        self.info(request, f'checking token {request.auth} for service {self.service}')
        return Response(status = st.HTTP_200_OK)

    def post(self, request: Request, format: str = 'json') -> Response:
        self.info(request, f'requesting token for service {self.service}')

        serializer = self.token_serializer(data = request.data, context = {'request': request})
        serializer.is_valid()

        token = self.token_model.objects.create()

        return Response(data = {'token': token.token}, status = st.HTTP_200_OK)

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

class PostRSSParserAuthView(TokenView):
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