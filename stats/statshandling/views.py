from generic.views import BaseView

from .models import GenericStat
from .serializers import GenericStatSerializer

from rest_framework.views import Request, Response
import rest_framework.status as st



class BaseStatView(BaseView):
    model = GenericStat
    serializer = GenericStatSerializer
    service = ''

    def post(self, request: Request, format: str = 'json') -> Response:
        self.info(request, f"adding stats for service [{self.service}]")

        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=st.HTTP_202_ACCEPTED)

        self.exception(request, f'not valid data for serializer : {serializer.errors}')
        return Response(data=serializer.errors, status=st.HTTP_400_BAD_REQUEST)
