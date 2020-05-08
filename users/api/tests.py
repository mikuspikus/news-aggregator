from django.urls import reverse

from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate, APIClient

from uuid import uuid4

from .views import UsersView, UserView
from .models import User


# class IntegrationTestCase(APITestCase):
#     def setUp(self):
#         self.users = 'users', UsersView.as_view()
#         self.user = 'user', UserView.as_view()

#         self.factory = APIRequestFactory()

#         self.owner = uuid4()

#         self.auth_owner = {'uuid': str(self.owner), 'username': 'username',
#                            'token': 'token', 'is_staff': False}

#         self.data = {
#             'username': 'username',
#             'email': 'email@mail.com',
#             'password': 'How to unit test permissions in django-rest-framework?'
#         }

#     def test_patch_user_by_owner(self):
#         user = User.objects.create(**self.data)

#         url, view = self.user
#         request = self.factory.patch(url + '/' + str(user.id), self.data)

#         auth = self.auth_owner
#         auth['uuid'] = str(user.id)

#         force_authenticate(request, token=auth)

#         response = view(request, user.id)
#         print(response.data)
#         self.assertEqual(response.status_code, 202)

#     def test_patch_comment_by_not_owner(self):
#         user = User.objects.create(**self.data)

#         url, view = self.user
#         request = self.factory.patch(url + '/' + str(user.id), self.data)

#         auth = self.auth_owner
#         auth['uuid'] = str(uuid4)

#         force_authenticate(request, token=auth)

#         response = view(request, user.id)
#         self.assertEqual(response.status_code, 403)
