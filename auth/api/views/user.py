from django.shortcuts import render

from ..models import (
    UserAuthToken,
    AuthUser,
)
from ..authentication import (
    UserTokenAuthentication,
    UserCredentialsAuthentication,
    ServicesAuthentication,
)

from ..serializers.user import UserSerializer

from generic.views import BaseView

from rest_framework.views import Request, Response
import rest_framework.status as st
from rest_framework.permissions import IsAuthenticated

class UsersView(BaseView):
    model = AuthUser
    serializer = UserSerializer
    permission_classes = []
    authentication_classes = (ServicesAuthentication,)

    def post(self, request: Request) -> Response:
        self.info(request, f"adding object")

        serializer_ = self.serializer(data=request.data)

        if serializer_.is_valid():
            serializer_.save()

            return Response(data=serializer_.data, status=st.HTTP_201_CREATED)

        self.exception(request, f"not valid data for serializer : {serializer_.errors}")
        return Response(data=serializer_.errors, status=st.HTTP_400_BAD_REQUEST)


class AuthTokenView(BaseView):
    authentication_classes = (UserTokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get(self, request: Request, format: str = "json") -> Response:
        self.info(request, f"checking logged-in user token {request.auth}")
        return Response(
            data={"uuid": request.user.uuid, "is_staff": request.user.is_staff, 'username': request.user.username},
            status=st.HTTP_200_OK,
        )


class UserView(BaseView):
    model = AuthUser
    authentication_classes = (UserTokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    serializer = UserSerializer

    def patch(self, request: Request, uuid: str, format: str = "json") -> Response:
        self.info(request, f"token ({request.auth}) changing user ({uuid}) credentials")
        try:
            row_ = self.model.objects.get(uuid=uuid)

        except self.model.DoesNotExist as error:
            self.exception(f"object with id : {uuid} not found")
            return Response(status=st.HTTP_404_NOT_FOUND)

        serializer_ = self.serializer(instance=row_, data=request.data)

        if serializer_.is_valid():
            serializer_.save()

            return Response(data=serializer_.data, status=st.HTTP_202_ACCEPTED)

        self.exception(request, f"not valid data for serializer : {serializer_.errors}")
        return Response(data=serializer_.errors, status=st.HTTP_400_BAD_REQUEST)


class UserLoginView(BaseView):
    authentication_classes = (UserCredentialsAuthentication,)
    permission_classes = (IsAuthenticated, )
    token_model = UserAuthToken

    def post(self, request: Request, format: str = "json") -> Response:
        self.info(request, f"user '{request.user.username}' requested for token")

        token, created = self.token_model.objects.get_or_create(user=request.user)

        return Response(
            data={
                "token": token.token,
                "uuid": request.user.uuid,
                "username": request.user.username,
                "is_superuser": request.user.is_superuser,
            },
            status=st.HTTP_200_OK,
        )
