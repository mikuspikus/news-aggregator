from django.urls import reverse

from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate, APIClient

from uuid import uuid4

from .views import CommentsView, CommentView
from .models import Comment


class IntegrationTestCase(APITestCase):
    def setUp(self):
        self.comments = 'comments', CommentsView.as_view()
        self.comment = 'comment', CommentView.as_view()

        self.factory = APIRequestFactory()

        self.owner = uuid4()

        self.auth_owner = {'uuid': str(self.owner), 'username': 'username',
                           'token': 'token', 'is_staff': False}

        self.data = {
            'author': self.owner,
            'news': uuid4(),
            'body': 'How to unit test permissions in django-rest-framework?'
        }

    def test_post_new_comment(self):
        url, view = self.comments
        request = self.factory.post(url, self.data)
        force_authenticate(request, token=self.auth_owner)

        response = view(request)

        self.assertEqual(response.status_code, 201)

    def test_patch_comment_by_owner(self):
        comment = Comment.objects.create(**self.data)

        url, view = self.comment
        request = self.factory.patch(url + '/' + str(comment.id), self.data)

        force_authenticate(request, token=self.auth_owner)

        response = view(request, comment.id)
        self.assertEqual(response.status_code, 202)

    def test_patch_comment_by_not_owner(self):
        comment = Comment.objects.create(**self.data)

        url, view = self.comment
        request = self.factory.patch(url + '/' + str(comment.id), self.data)

        auth = self.auth_owner
        auth['uuid'] = str(uuid4)

        force_authenticate(request, token=auth)

        response = view(request, comment.id)
        self.assertEqual(response.status_code, 403)
