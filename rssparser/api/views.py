from uuid import UUID
from generic.views import BaseView

from .models import Feed
from .serializers import FeedSerializer
from .authentication import TokenAuthentication
from .permissions import IsAuthorizedAndFeedOwner, IsAuthenticatedFor, IsAuthorizedAndFeedsOwner

from celery import Celery
from queueconfig.celeryconfig import Config

from rest_framework.views import Request, Response
import rest_framework.status as st

import feedparser as fp


class FeedBaseView(BaseView):
    celery = Celery()
    task = 'tasks.stats.rssparser'

    def __init__(self, **kwargs):
        self.celery.config_from_object(Config)
        super().__init__(**kwargs)

    def send_task(self, action: str, user: UUID = None, input: dict = None, output: dict = None):
        self.celery.send_task(self.task, [user, action, input, output])


class FeedParseView(FeedBaseView):
    model = Feed
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthorizedAndFeedOwner, )

    def get(self, request: Request, pk: int, fromat: str = 'json') -> Response:
        self.info(request, f"requested for parsed feed {pk}")

        feed = self.get_object(request, pk)
        parsed_feed = fp.parse(feed.url)

        user = request.auth.get('uuid') if request.auth else None
        self.send_task('GET', user, output = {'status': parsed_feed.status})

        status = parsed_feed.get('status')
        if status == 200:
            return Response(data=parsed_feed, status=status)

        msg = parsed_feed.bozo_exception.getMessage()
        self.exception(request, f"failed to parse feed with error : {msg}")

        return Response(data = {'error': msg}, status = status)



# class FeedsParseView(FeedBaseView):
#     model = Feed
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthorizedAndFeedsOwner,)

#     def get_objects(self, request: Request, user: UUID) -> Feed:
#         return self.model.objects.filter(user=user)

#     def get(self, request: Request, user: UUID, format: str = 'json') -> Response:
#         self.info(request, f"requested for user ({user}) feeds")

#         feeds = self.get_objects(request, user)
#         parsed_feeds = [fp.parse(feed.url) for feed in feeds]
#         user = request.auth.get('uuid') if request.auth else None
#         self.send_task(action='GET', user=user, output={
#                        'length': len(parsed_feeds)})

#         return Response(data=parsed_feeds, status=st.HTTP_200_OK)


class FeedView(FeedBaseView):
    model = Feed
    serializer = FeedSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticatedFor, IsAuthorizedAndFeedOwner)

    def get(self, request: Request, pk: int, format: str = 'json') -> Response:
        self.info(request, f'asked for object with pk : {pk}')

        obj = self.get_object(request, pk)
        serializer_ = self.serializer(instance=obj)
        user = request.auth.get('uuid') if request.auth else None
        self.send_task(action='GET', user=user, output=serializer_.data)

        return Response(data=serializer_.data, status=st.HTTP_200_OK)

    def patch(self, request: Request, pk: int, format: str = 'json') -> Response:
        self.info(request, f'asked to modify object with id : {pk}')

        obj = self.get_object(request, pk)
        old_objserializer = self.serializer(instance=obj, partial=True)
        serializer_ = self.serializer(instance=obj, data=request.data, partial=True)
        user = request.auth.get('uuid') if request.auth else None

        if serializer_.is_valid():
            serializer_.save()

            self.send_task(action='PATCH', user=user,
                           input=old_objserializer.data, output=serializer_.data)

            return Response(data=serializer_.data, status=st.HTTP_202_ACCEPTED)

        self.exception(
            request, f'not valid data for serializer : {serializer_.errors}')

        self.send_task(action='PATCH', user=user,
                       input=old_objserializer.data, output=serializer_.errors)
        return Response(data=serializer_.errors, status=st.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int, format: str = 'json') -> Response:
        self.info(request, f'asked to delete object with id : {pk}')

        obj = self.get_object(request, pk)
        serializer = self.serializer(instance=obj)
        obj.delete()
        user = request.auth.get('uuid') if request.auth else None
        self.send_task(name='DELETE', user=user, output=serializer.data)

        return Response(status=st.HTTP_204_NO_CONTENT)


class FeedsView(FeedBaseView):
    model = Feed
    serializer = FeedSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorizedAndFeedOwner,)

    def post(self, request: Request) -> Response:
        self.info(request, f'adding object')

        serializer_ = self.serializer(data=request.data)
        user = request.auth.get('uuid') if request.auth else None
        if serializer_.is_valid():
            serializer_.save()

            self.send_task(action='POST', user=user, output=serializer_.data)

            return Response(data=serializer_.data, status=st.HTTP_202_ACCEPTED)

        self.exception(
            request, f'not valid data for serializer : {serializer_.errors}')

        user = request.auth.get('uuid') if request.auth else None
        self.send_task(action='POST', user=user, output=serializer_.errors)
        return Response(data=serializer_.errors, status=st.HTTP_400_BAD_REQUEST)

    def get(self, request: Request) -> Response:
        self.info(request, f'request objects')

        row_s_ = self.model.objects.all()

        user = request.query_params.get('user')
        if user:
            row_s_ = row_s_.filter(user=user)

        serializer_ = self.serializer(row_s_, many=True)
        user = request.auth.get('uuid') if request.auth else None
        self.send_task(action='GET', user=user, output={
                       'length': len(serializer_.data)})

        return Response(data=serializer_.data, status=st.HTTP_200_OK)
