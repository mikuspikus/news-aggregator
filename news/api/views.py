from django.shortcuts import render

from rest_framework.views import Request, Response
import rest_framework.status as st

from .models import News, User, Vote
from .serializers import NewsSerializer
from .authentication import TokenAuthentication

from uuid import UUID

from generic.views import BaseView
from .permissions import IsAuthenticatedFor, IsAuthorizedAndNewsOwner
from remoteauth.permissions import IsRemoteAuthenticated

from django.conf import settings

SCORE_CHANGE = getattr(settings, 'SCORE_CHANGE', 0.2)


class NewsVoteView(BaseView):
    model = News
    user = User
    vote = Vote
    serializer = NewsSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsRemoteAuthenticated, )

    def post(self, request: Request, pk: UUID, format: str = 'json') -> Response:
        self.info(request, f'change score of news with pk : {pk}')

        if 'is_up' not in request.data:
            return Response(data={'error': "Parameter 'is_up' not found"}, status=st.HTTP_400_BAD_REQUEST)

        is_up = bool(request.data.get('is_up'))

        news = self.get_object(request, pk)
        u_uuid = request.auth['uuid']

        user, created = self.user.objects.get_or_create(uuid=u_uuid)
        vote, created = self.vote.objects.get_or_create(news=news, user=user)

        if created:
            news.score += SCORE_CHANGE if is_up else -SCORE_CHANGE
            vote.is_up = is_up

            news.save()
            vote.save()
            

        else:
            if vote.is_up != is_up:
                vote.is_up = is_up
                news.score += 2 * SCORE_CHANGE if is_up else -2 * SCORE_CHANGE

                vote.save()
                news.save()

        serializer = self.serializer(instance=news)

        return Response(data=serializer.data, status=st.HTTP_202_ACCEPTED)


class SingleNewsView(BaseView):
    model = News
    serializer = NewsSerializer
    #authentication_classes = (TokenAuthentication, )
    #permission_classes = (IsAuthenticatedFor, IsAuthorizedAndNewsOwner)

    def get(self, request: Request, pk: UUID, format: str = 'json') -> Response:
        self.info(request, f'asked for object with pk : {pk}')

        obj = self.get_object(request, pk)
        serializer_ = self.serializer(instance=obj)

        return Response(data=serializer_.data, status=st.HTTP_200_OK)

    def patch(self, request: Request, pk: UUID, format: str = 'json') -> Response:
        self.info(request, f'asked to modify object with id : {pk}')

        obj = self.get_object(request, pk)
        serializer_ = self.serializer(instance=obj, data=request.data)

        if serializer_.is_valid():
            serializer_.save()

            return Response(data=serializer_.data, status=st.HTTP_202_ACCEPTED)

        self.exception(
            request, f'not valid data for serializer : {serializer_.errors}')
        return Response(data=serializer_.errors, status=st.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: UUID, format: str = 'json') -> Response:
        self.info(request, f'asked to delete object with id : {pk}')

        obj = self.get_object(request, pk)
        obj.delete()

        return Response(status=st.HTTP_204_NO_CONTENT)


class MultiNewsView(BaseView):
    model = News
    serializer = NewsSerializer

    permission_classes = []
    authentication_classes = []

    def post(self, request: Request) -> Response:
        self.info(request, f'adding object')

        serializer_ = self.serializer(data=request.data)

        if serializer_.is_valid(raise_exception=True):
            serializer_.save()

            return Response(data=serializer_.data, status=st.HTTP_201_CREATED)

        self.exception(
            request, f'not valid data for serializer : {serializer_.errors}')
        return Response(data=serializer_.errors, status=st.HTTP_400_BAD_REQUEST)

    def get(self, request: Request) -> Response:
        self.info(request, f'request objects')

        row_s_ = self.model.objects.all()

        serializer_ = self.serializer(data=row_s_, many=True)

        return Response(data=serializer_.data, status=st.HTTP_200_OK)
