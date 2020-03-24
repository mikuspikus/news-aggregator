from django.shortcuts import render

from .models import User
from .serializers import UserSerializer
from .authentication import RemoteTokenAuthentication

from rest_framework.views import APIView, Request, Response
import rest_framework.status as st

from uuid import UUID

from remoteauth.permissions import IsRemoteAuthenticated
from .permissions import IsAuthorizedAndUser
from generic.views import BaseView


class UserView(BaseView):
    model = User
    serializer = UserSerializer
    permission_classes = (IsAuthorizedAndUser, )

    def get(self, request: Request, id_: UUID, format: str = 'json') -> Response:
        self.info(request, f'asked for object with id : {id_}')

        obj = self.get_object(request, id_)
        serializer_ = self.serializer(instance=obj)

        return Response(data=serializer_.data, status=st.HTTP_200_OK)

    def patch(self, request: Request, id_: UUID, format: str = 'json') -> Response:
        self.info(request, f'asked to modify object with id : {id_}')

        obj = self.get_object(request, id_)
        serializer_ = self.serializer(instance=obj, data=request.data)

        if serializer_.is_valid():
            serializer_.save()

            return Response(data=serializer_.data, status=st.HTTP_202_ACCEPTED)

        self.exception(
            request, f'not valid data for serializer : {serializer_.errors}')
        return Response(data=serializer_.errors, status=st.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id_: UUID, format: str = 'json') -> Response:
        self.info(request, f'asked to delete object with id : {id_}')

        obj = self.get_object(request, id_)
        obj.delete()

        return Response(status=st.HTTP_204_NO_CONTENT)


class UsersView(BaseView):
    model = User
    serializer = UserSerializer

    permission_classes = [IsRemoteAuthenticated]
    authentication_classes = [RemoteTokenAuthentication]

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
