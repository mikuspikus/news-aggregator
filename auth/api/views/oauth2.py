from oauth2_provider.contrib.rest_framework.authentication import OAuth2Authentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Request, Response
import rest_framework.status as st

from generic.views import BaseView

# http://127.0.0.1:8080/oauth2/authorize/?client_id=Lm07c3cveewrcbcBwt0h4erkifIz1fyT0oMLvcR0&response_type=code

class OAuth2TokenView(BaseView):
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request, format: str = "json") -> Response:
        self.info(request, f"fetching OAuth2 token {request.auth} user")
        user = request.user
        return Response(
            data={
                "username": user.username,
                "uuid": user.uuid,
                "is_staff": user.is_staff,
            },
            status=st.HTTP_200_OK
        )

