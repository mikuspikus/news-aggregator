from oauth2_provider.contrib.rest_framework.authentication import OAuth2Authentication

from generic.views import BaseView

from rest_framework.views import Request, Response
import rest_framework.status as st

from gateway.requesters import exchange_code_oauth2

from django.conf import settings


class BasePublicView(BaseView):
    ERROR_FIELD = getattr(settings, 'ERROR_FIELD', 'error')
    authentication_classes = []
    permission_classes = []


class CodeExchangeView(BasePublicView):
    def post(self, request: Request, format: str = 'json') -> Response:
        self.info(request, f"exchanging code")

        code = request.data.get('code')
        if not code:
            self.exception(request, f"'\'code\' not found'")
            return Response(data={self.ERROR_FIELD: '\'code\' not found'}, status=st.HTTP_400_BAD_REQUEST)

        response, status = exchange_code_oauth2(code)
        return Response(response, status)
