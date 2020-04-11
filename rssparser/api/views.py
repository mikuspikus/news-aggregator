from uuid import UUID
from generic.views import BaseView

from .models import Feed
from .serializers import FeedSerializer
from .authentication import TokenAuthentication
from .permissions import IsAuthorizedAndFeedOwner, IsAuthenticatedFor, IsAuthorizedAndFeedsOwner


from rest_framework.views import Request, Response
import rest_framework.status as st

import feedparser as fp


class FeedParserView(BaseView):
    model = Feed
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorizedAndFeedsOwner,)

    def get_object(self, request: Request, user: UUID) -> Feed:
        feed = self.model.objects.filter(user = user)

    def get(self, request: Request, user: UUID, format: str = 'json') -> Response:
        self.info(request, f"requested for user ({user}) feeds")

        feeds = self.get_object(request, user)
        parsed_feeds = [fp.parse(feed.url) for feed in feeds]

        return Response(data = parsed_feeds, status = st.HTTP_200_OK)


class FeedsView(BaseView):
    model = Feed
    serializer = FeedSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticatedFor, IsAuthorizedAndFeedOwner)

    def get(self, request: Request, pk: int, format: str = 'json') -> Response:
        self.info(request, f'asked for object with pk : {pk}')

        obj = self.get_object(request, pk)
        serializer_ = self.serializer(instance=obj)

        return Response(data=serializer_.data, status=st.HTTP_200_OK)

    def patch(self, request: Request, pk: int, format: str = 'json') -> Response:
        self.info(request, f'asked to modify object with id : {pk}')

        obj = self.get_object(request, pk)
        serializer_ = self.serializer(instance=obj, data=request.data)

        if serializer_.is_valid():
            serializer_.save()

            return Response(data=serializer_.data, status=st.HTTP_202_ACCEPTED)

        self.exception(
            request, f'not valid data for serializer : {serializer_.errors}')
        return Response(data=serializer_.errors, status=st.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int, format: str = 'json') -> Response:
        self.info(request, f'asked to delete object with id : {pk}')

        obj = self.get_object(request, pk)
        obj.delete()

        return Response(status=st.HTTP_204_NO_CONTENT)


class FeedView(BaseView):
    model = Feed
    serializer = FeedSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorizedAndFeedOwner,)

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
