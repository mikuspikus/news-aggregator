from django.shortcuts import render

from ..models import (
    UserAuthToken,
    AuthUser,
)
from ..authentication import (
    AuthAuthentication,
    UserCredentialsAuthentication,
)

from ..tokenauthentication.permissions import IsAuthenticatedForMethods

from ..serializers.user import UserSerializer

from ..base.views import BaseView


from rest_framework.views import Request, Response
import rest_framework.status as st


class UsersView(BaseView):
    model = AuthUser
    serializer = UserSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request: Request) -> Response:
        self.info(request, f"adding object")

        serializer_ = self.serializer(data=request.data)

        if serializer_.is_valid():
            serializer_.save()

            return Response(data=serializer_.data, status=st.HTTP_201_CREATED)

        self.exception(request, f"not valid data for serializer : {serializer_.errors}")
        return Response(data=serializer_.errors, status=st.HTTP_400_BAD_REQUEST)


class UserView(BaseView):
    model = AuthUser
    authentication_classes = (AuthAuthentication,)
    serializer = UserSerializer

    def patch(self, request: Request, uuid: str, format: str = "json") -> Response:
        self.info(request, f"token ({request.auth}) changing user ({uuid}) credentials")
        try:
            row_ = self.model.objects.get(pk=uuid)

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
    token_model = UserAuthToken

    def post(self, request: Request, format: str = "json") -> Response:
        self.info(request, f"user '{request.user.username}' requested for token")

        token, created = self.token_model.objects.get_or_create(user=request.user)

        return Response(data={"token": token.token}, status=st.HTTP_200_OK)


class AuthTokenView(BaseView):
    authentication_classes = (AuthAuthentication,)

    def get(self, request: Request, format: str = "json") -> Response:
        self.info(request, f"checking logged-in user token {request.auth}")

        return Response(status=st.HTTP_200_OK)