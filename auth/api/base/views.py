from logging import getLogger
from rest_framework.views import APIView, Request


class BaseView(APIView):
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