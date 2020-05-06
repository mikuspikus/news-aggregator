from generic.views import BaseView

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Request, Response
import rest_framework.status as st

from gateway.authentication import OAuth2TokenAuthentication
import gateway.requesters as requesters

from uuid import UUID


class ProtectedBaseView(BaseView):
    authentication_classes = (OAuth2TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class UserView(ProtectedBaseView):
    service = 'user'

    def patch(self, request: Request, format: str = 'json') -> Response:
        self.info(request, f"patching user {request.auth.get('uuid')}")

        json, code = requesters.patch_user(
            token=request.auth.get('token'),
            useruuid=request.auth.get('uuid'),
            userdata=request.data
        )

        return Response(json, code)


class MultiNewsView(ProtectedBaseView):
    service = 'news'

    def post(self, request: Request, format: str = 'json') -> Response:
        self.info(request, f"adding news by user {request.auth.get('uuid')}")

        json, code = requesters.add_news(
            token=request.auth.get('token'),
            newsdata=request.data,
        )

        return Response(json, code)

    def get(self, request: Request, format: str = 'json') -> Response:
        self.info(
            request, f"fetching news for user {request.auth.get('uuid')}")

        page = request.query_params.get('page', 1)
        json, code = requesters.news(
            token=request.auth.get('token'),
            page=page
        )

        return Response(json, code)


class SingleNewsView(ProtectedBaseView):
    service = 'news'

    def get(self, request: Request, newsuuid: UUID, format: str = 'json') -> Response:
        self.info(
            request, f"fetching sinle news {newsuuid} for user {request.auth.get('uuid')}")

        json, code = requesters.single_news(
            token=request.auth.get('token'),
            newsuuid=newsuuid
        )

        return Response(json, code)

    def patch(self, request: Request, newsuuid: UUID, format: str = 'json') -> Response:
        self.info(
            request, f"patching news {newsuuid} by user {request.auth.get('uuid')}")

        json, code = requesters.patch_news(
            token=request.auth.get('token'),
            newsuuid=newsuuid,
            newsdata=request.data
        )

        return Response(json, code)


class CommentView(ProtectedBaseView):
    # def get(self, request: Request, commentid: int, format: str = 'json') -> Response:
    #     self.info(request, f"fetching comment {commentid} for user {request.auth.get('uuid')}")

    #     json, code = requesters.co

    def pacth(self, request: Request, commentid: int, format: str = 'json') -> Response:
        self.info(
            request, f"patching comment {commentid} by user {request.auth.get('uuid')}")

        json, code = requesters.patch_comment(
            token=request.auth.get('token'),
            commentid=commentid,
            commentdata=request.data
        )

        return Response(json, code)


class CommentsView(ProtectedBaseView):
    def get(self, request: Request, fromat: str = 'json') -> Response:
        self.info(
            request, f"fetching comments for user {request.auth.get('uuid')}")

        newsuuid = request.query_params.get('news')

        if not newsuuid:
            msg = "'news' query parameter not found"
            self.exception(request, msg)
            return Response({'error': msg}, status=st.HTTP_400_BAD_REQUEST)

        json, code = requesters.comments(
            token=request.auth.get('token'),
            newsuuid=newsuuid
        )

        return Response(json, code)

    def post(self, request: Request, format: str = 'json') -> Response:
        self.info(request, f"adding comment by user {request.auth.get('uuid')}")

        json, code = requesters.add_comment(
            token=request.auth.get('token'),
            commentdata=request.data
        )

        return Response(json, code)


class VoteView(ProtectedBaseView):
    def post(self, request: Request, newsuuid: UUID, format: str = 'json') -> Response:
        self.info(request, f"user {request.auth.get('uuid')} voting news {newsuuid}")

        json, code = requesters.vote_news(
            token=request.auth.get('token'),
            newsuuid=newsuuid,
            votedata=request.data
        )

        return Response(json, code)