from django.urls import reverse
from django.conf import settings

from rest_framework.test import APITestCase

from .models import AuthUser, UserAuthToken, ServicesToken


class ServiceServiceTokenTest(APITestCase):
    CREDETNTIALS = settings.CREDENTIALS
    token_model = ServicesToken

    def test_get_token(self):
        data = {
            "id": self.CREDETNTIALS["AUTH"]["ID"],
            "secret": self.CREDETNTIALS["AUTH"]["SECRET"],
        }
        response = self.client.post(reverse("tokens"), data)

        self.assertEqual(response.status_code, 200)

    def test_check_token(self):
        token = self.token_model.objects.create()
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.token)
        response = self.client.get(reverse('tokens'))

        self.assertEqual(response.status_code, 200)

class UserTokenAuthentication(APITestCase):
    token_model = UserAuthToken
    user_model = AuthUser

    def setUp(self):
        self.userdata = {'username': 'username', 'password': 'userpassword'}
        self.user = self.user_model.objects.create_user(**self.userdata)

    def test_get_token(self):
        response = self.client.post(reverse('user-login'), data = self.userdata)
        self.assertEqual(response.status_code, 200)

    def test_check_token(self):
        token = self.token_model.objects.create(user = self.user)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.token)
        response = self.client.get(reverse('user-logged-in'))
        self.assertEqual(response.status_code, 200)

