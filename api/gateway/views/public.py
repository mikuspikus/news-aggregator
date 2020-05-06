from oauth2_provider.contrib.rest_framework.authentication import OAuth2Authentication

from generic.views import BaseView

from rest_framework.views import Request, Response
import rest_framework.status as st

from gateway.requesters import exchange_code_oauth2, refresh_token_oauth2 #, revoke_token_oauth2

from django.conf import settings


class PublicBaseView(BaseView):
    ERROR_FIELD = getattr(settings, 'ERROR_FIELD', 'error')
    authentication_classes = []
    permission_classes = []


class CodeExchangeView(PublicBaseView):
    def get(self, request: Request, format: str = 'json') -> Response:
        self.info(request, f"exchanging code")

        code = request.query_params.get('code')
        if not code:
            msg = "'code' not found"
            self.exception(request, msg)
            return Response(data={self.ERROR_FIELD: msg}, status=st.HTTP_400_BAD_REQUEST)

        json, code = exchange_code_oauth2(code)
        return Response(data=json, status=code)