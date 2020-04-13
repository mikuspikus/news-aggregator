from celery import Celery
from queueconfig.celeryconfig import Config

from .models import User
from .serializers import UserSerializer
from .authentication import TokenAuthentication

from rest_framework.views import APIView, Request, Response
import rest_framework.status as st

from uuid import UUID

from remoteauth.permissions import IsRemoteAuthenticated
from .permissions import IsAuthorizedAndUser
from generic.views import BaseView

class UserBaseView(BaseView):
    celery = Celery()
    task = 'tasks.stats.user'

    def __init__(self, **kwargs):
        self.celery.config_from_object(Config)
        super().__init__(**kwargs)

    def send_task(self, action: str, user: UUID = None, input: dict = None, output: dict = None):
        self.celery.send_task(self.task, [user, action, input, output])


class UserView(UserBaseView):
    model = User
    serializer = UserSerializer
    permission_classes = (IsAuthorizedAndUser, )

    def get(self, request: Request, pk: UUID, format: str = 'json') -> Response:
        self.info(request, f'asked for object with pk : {pk}')

        obj = self.get_object(request, pk)
        serializer_ = self.serializer(instance=obj)

        self.send_task(action = 'GET', user = request.auth.get('uuid'), output = serializer_.data)

        return Response(data=serializer_.data, status=st.HTTP_200_OK)

    def patch(self, request: Request, pk: UUID, format: str = 'json') -> Response:
        self.info(request, f'asked to modify object with id : {pk}')

        obj = self.get_object(request, pk)
        old_objserializer = self.serializer(instance=obj)
        serializer_ = self.serializer(instance=obj, data=request.data)

        if serializer_.is_valid():
            serializer_.save()

            self.send_task(action = 'PATCH', user = request.auth.get('uuid'), input = old_objserializer.data, output = serializer_.data)

            return Response(data=serializer_.data, status=st.HTTP_202_ACCEPTED)

        self.exception(
            request, f'not valid data for serializer : {serializer_.errors}')

        self.send_task(action = 'PATCH', user = request.auth.get('uuid'), input = old_objserializer.data, output = serializer_.errors)
        return Response(data=serializer_.errors, status=st.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: UUID, format: str = 'json') -> Response:
        self.info(request, f'asked to delete object with id : {pk}')

        obj = self.get_object(request, pk)
        serializer = self.serializer(instance=obj)
        obj.delete()
        self.send_task(name = 'DELETE', user = request.auth.get('uuid'), output = serializer.data)

        return Response(status=st.HTTP_204_NO_CONTENT)


class UsersView(UserBaseView):
    model = User
    serializer = UserSerializer

    permission_classes = [IsRemoteAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request: Request) -> Response:
        self.info(request, f'adding object')

        serializer_ = self.serializer(data=request.data)

        if serializer_.is_valid():
            serializer_.save()

            self.send_task(action = 'POST', user = request.auth.get('uuid'), output = serializer_.data)

            return Response(data=serializer_.data, status=st.HTTP_202_ACCEPTED)

        self.exception(
            request, f'not valid data for serializer : {serializer_.errors}')

        self.send_task(action = 'POST', user = request.auth.get('uuid'), output = serializer_.errors)
        return Response(data=serializer_.errors, status=st.HTTP_400_BAD_REQUEST)

    def get(self, request: Request) -> Response:
        self.info(request, f'request objects')

        row_s_ = self.model.objects.all()

        serializer_ = self.serializer(data=row_s_, many=True)
        user = request.auth.get('uuid') if request.auth else None
        self.send_task(name = 'GET', user = user, output = {'length' : len(serializer_.data)})

        return Response(data=serializer_.data, status=st.HTTP_200_OK)
