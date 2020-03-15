from django.shortcuts import render

from .models import CustomUser
from .serializers import CustomUserSerializer
from .authentication import RemoteTokenAuthentication
from .permissions import IsRemoteAuthenticated

from rest_framework.views import APIView, Request, Response
import rest_framework.status as st

from logging import getLogger

class BaseView(APIView):
    authentication_classes = (RemoteTokenAuthentication, )
    permission_classes = []
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

class UserView(BaseView):
    model = CustomUser
    serializer = CustomUserSerializer
    permission_classes = (IsRemoteAuthenticated, )

    def get(self, request: Request, id_: int, format: str = 'json') -> Response:
        self.info(request, f'asked for object with id : {id_}')

        try:
            row_ = self.model.objects.get(pk = id_)

        except self.model.DoesNotExist:
            self.exception(f'object with id : {id_} not found')
            return Response(status = st.HTTP_404_NOT_FOUND)

        serializer_ = self.serializer(instance = row_)
        return Response(data = serializer_.data, status = st.HTTP_200_OK)

    def patch(self, request: Request, id_: int, format: str = 'json') -> Response:
        self.info(request, f'asked to modify object with id : {id_}')

        try:
            row_ = self.model.objects.get(pk = id_)

        except self.model.DoesNotExist as error:
            self.exception(f'object with id : {id_} not found')
            return Response(status = st.HTTP_404_NOT_FOUND)

        serializer_ = self.serializer(instance = row_, data = request.data)

        if serializer_.is_valid():
            serializer_.save()

            return Response(data = serializer_.data, status = st.HTTP_202_ACCEPTED)

        self.exception(request, f'not valid data for serializer : {serializer_.errors}')
        return Response(data = serializer_.errors, status = st.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id_: int, format: str = 'json') -> Response:
        self.info(request, f'asked to delete object with id : {id_}')

        try:
            row_ = self.model.objects.get(pk = id_)

        except self.model.DoesNotExist:
            self.exception(f'object with id : {id_} not found')
            return Response(status = st.HTTP_404_NOT_FOUND)

        row_.delete()
        return Response(status = st.HTTP_204_NO_CONTENT)

class UsersView(BaseView):
    model = CustomUser
    serializer = CustomUserSerializer

    permission_classes = []
    authentication_classes = []


    def post(self, request: Request) -> Response:
        self.info(request, f'adding object')

        serializer_ = self.serializer(data = request.data)

        if serializer_.is_valid():
            serializer_.save()

            return Response(data = serializer_.data, status = st.HTTP_201_CREATED)

        self.exception(request, f'not valid data for serializer : {serializer_.errors}')
        return Response(data = serializer_.errors, status = st.HTTP_400_BAD_REQUEST)

    def get(self, request: Request) -> Response:
        self.info(request, f'request objects')

        row_s_ = self.model.objects.all()

        serializer_ = self.serializer(data = row_s_, many = True)

        return Response(data = serializer_.data, status = st.HTTP_200_OK)
