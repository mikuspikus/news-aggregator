from rest_framework.views import Request, Response
import rest_framework.status as st

from celery import Celery

from remoteauth.permissions import IsRemoteAuthenticated
from generic.views import BaseView
from queueconfig.celeryconfig import Config

from .models import News, User, Vote
from .serializers import NewsSerializer
from .authentication import TokenAuthentication, OAuth2TokenAuthentication
from .permissions import IsAuthenticatedFor, IsAuthorizedAndNewsOwner
from .pagination import PageNumberPaginationTotalPages


from uuid import UUID


from django.conf import settings

SCORE_CHANGE = getattr(settings, 'SCORE_CHANGE', 0.2)


class BaseNewsView(BaseView):
    authentication_classes = (TokenAuthentication, OAuth2TokenAuthentication)
    celery = Celery()
    task = 'tasks.stats.news'

    def __init__(self, **kwargs):
        self.celery.config_from_object(Config)
        super().__init__(**kwargs)

    def send_task(self, action: str, user: UUID = None, input: dict = None, output: dict = None):
        self.celery.send_task(self.task, [user, action, input, output])


class NewsVoteView(BaseNewsView):
    model = News
    user = User
    vote = Vote
    serializer = NewsSerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (IsRemoteAuthenticated, )

    def get(self, request: Request, pk: UUID, format: str = 'json') -> Response:
        self.info(
            request, f"user {request.auth.get('uuid')}  asking for his votes to news {pk}")

        news = self.get_object(request, pk)
        user, created = self.user.objects.get_or_create(uuid = request.auth['uuid'])
        response = {'upvoted': False, 'downvoted': False}

        try:
            vote = self.vote.objects.get(news=news, user=user)

        except self.vote.DoesNotExist as error:
            return Response(data = response, status = st.HTTP_200_OK)

        if vote.is_up:
            response['upvoted'] = True

        else:
            response['downvoted'] = True

        return Response(data = response, status=st.HTTP_200_OK)

    def post(self, request: Request, pk: UUID, format: str = 'json') -> Response:
        self.info(request, f'change score of news with pk : {pk}')

        if 'is_up' not in request.data:
            return Response(data={'error': "Parameter 'is_up' not found"}, status=st.HTTP_400_BAD_REQUEST)

        is_up = bool(request.data.get('is_up'))

        news = self.get_object(request, pk)
        old_news_serializer = self.serializer(instance=news)

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

        self.send_task(action='POST', user=request.auth.get(
            'uuid'), input=old_news_serializer.data, output=serializer.data)

        return Response(data=serializer.data, status=st.HTTP_202_ACCEPTED)


class SingleNewsView(BaseNewsView):
    model = News
    serializer = NewsSerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticatedFor, IsAuthorizedAndNewsOwner)

    def get(self, request: Request, pk: UUID, format: str = 'json') -> Response:
        self.info(request, f'asked for object with pk : {pk}')

        obj = self.get_object(request, pk)
        serializer_ = self.serializer(instance=obj)
        user = request.auth.get('uuid') if request.auth else None
        self.send_task(action='GET', user=user, output=serializer_.data)

        return Response(data=serializer_.data, status=st.HTTP_200_OK)

    def patch(self, request: Request, pk: UUID, format: str = 'json') -> Response:
        self.info(request, f'asked to modify object with id : {pk}')

        obj = self.get_object(request, pk)
        old_objserializer = self.serializer(instance=obj)
        serializer_ = self.serializer(instance=obj, data=request.data)

        if serializer_.is_valid():
            serializer_.save()

            self.send_task(action='PATCH', user=request.auth.get(
                'uuid'), input=old_objserializer.data, output=serializer_.data)

            return Response(data=serializer_.data, status=st.HTTP_202_ACCEPTED)

        self.exception(
            request, f'not valid data for serializer : {serializer_.errors}')

        self.send_task(action='PATCH', user=request.auth.get(
            'uuid'), input=old_objserializer.data, output=serializer_.errors)
        return Response(data=serializer_.errors, status=st.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: UUID, format: str = 'json') -> Response:
        self.info(request, f'asked to delete object with id : {pk}')

        obj = self.get_object(request, pk)
        serializer = self.serializer(instance=obj)
        obj.delete()
        self.send_task(action='DELETE', user=request.auth.get(
            'uuid'), output=serializer.data)

        return Response(status=st.HTTP_204_NO_CONTENT)


class MultiNewsView(BaseNewsView):
    model = News
    serializer = NewsSerializer

    pagination_class = PageNumberPaginationTotalPages()
    permission_classes = (IsAuthenticatedFor,)
    # authentication_classes = (TokenAuthentication,)

    def post(self, request: Request, format: str = 'json') -> Response:
        self.info(request, f'adding object')

        data = request.data
        data['uuid'] = request.auth.get('uuid')

        serializer_ = self.serializer(data=data)

        if serializer_.is_valid():
            serializer_.save()

            self.send_task(action='POST', user=request.auth.get(
                'uuid'), output=serializer_.data)

            return Response(data=serializer_.data, status=st.HTTP_201_CREATED)

        self.exception(
            request, f'not valid data for serializer : {serializer_.errors}')

        self.send_task(action='POST', user=request.auth.get(
            'uuid'), output=serializer_.errors)
        return Response(data=serializer_.errors, status=st.HTTP_400_BAD_REQUEST)

    def paginate_queryset(self, queryset):
        return self.pagination_class.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        return self.pagination_class.get_paginated_response(data)

    def get(self, request: Request, format: str = 'json') -> Response:
        self.info(request, f'request objects')
        user = request.auth.get('uuid') if request.auth else None
        row_s_ = self.model.objects.all()
        page = self.paginate_queryset(row_s_)
        if page:
            serializer_ = self.serializer(page, many=True)

            self.send_task(action='GET', user=user, output={
                           'length': str(len(row_s_))})
            return self.get_paginated_response(serializer_.data)

        serializer_ = self.serializer(row_s_, many=True)
        self.send_task(action='GET', user=user, output={
                       'length': str(len(row_s_))})

        return Response(data=serializer_.data, status=st.HTTP_200_OK)
