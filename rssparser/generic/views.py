from logging import getLogger
from rest_framework.views import APIView, Request
from django.http import Http404

class BaseView(APIView):
    logger = getLogger('views')
    formatter = '{method} : {url} : {content_type} : {msg}'
    model = None
    serializer = None

    def get_object(self, request: Request, pk):
        try:
            obj = self.model.objects.get(pk=pk)

        except self.model.DoesNotExist as error:
            self.exception(f'object with id : {pk} not found')
            raise Http404

        self.check_object_permissions(request, obj)

        return obj

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