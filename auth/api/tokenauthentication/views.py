from ..base.views import BaseView
from .permissions import IsAuthenticatedForMethods

from rest_framework.views import Request, Response
import rest_framework.status as st

class TokenView(BaseView):
    token_model = None
    token_serializer = None
    permission_classes = (IsAuthenticatedForMethods, )
    authentication_classes = []
    service = ''

    def get(self, request: Request, format: str = 'json') -> Response:
        self.info(request, f'checking token {request.auth} for service {self.service}')
        return Response(status = st.HTTP_200_OK)

    def post(self, request: Request, format: str = 'json') -> Response:
        self.info(request, f'requesting token for service {self.service}')

        serializer = self.token_serializer(data = request.data, context = {'request': request})
        serializer.is_valid()

        token = self.token_model.objects.create()

        return Response(data = {'token': token.token}, status = st.HTTP_200_OK)