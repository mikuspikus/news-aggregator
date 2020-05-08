from django.urls import reverse

from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate, APIClient

from uuid import uuid4

from .views import MultiNewsView, SingleNewsView, NewsVoteView
from .models import News


class IntegrationTestCase(APITestCase):
    def setUp(self):
        self.multinews = 'multi-news', MultiNewsView.as_view()
        self.singlenews = 'single-news', SingleNewsView.as_view()
        self.newsvote = 'news-vote', NewsVoteView.as_view()

        self.factory = APIRequestFactory()

        self.owner = uuid4()

        self.auth_owner = {'uuid': str(self.owner), 'username': 'username',
                           'token': 'token', 'is_staff': False}

        self.data = {
            'author': self.owner,
            'url': 'https://stackoverflow.com/questions/33607701/django-test-doesnt-populate-request-auth',
            'title': 'How to unit test permissions in django-rest-framework?'
        }

    def test_post_new_news(self):
        url, view = self.multinews
        request = self.factory.post(url, self.data)
        force_authenticate(request, token=self.auth_owner)

        response = view(request)

        self.assertEqual(response.status_code, 201)

    def test_patch_news_by_owner(self):
        news = News.objects.create(**self.data)

        url, view = self.singlenews
        request = self.factory.patch(url + '/' + str(news.id), self.data)

        force_authenticate(request, token=self.auth_owner)

        response = view(request, news.id)
        self.assertEqual(response.status_code, 202)

    def test_patch_news_by_not_owner(self):
        news = News.objects.create(**self.data)
        url, view = self.singlenews
        request = self.factory.patch(url + '/' + str(news.id), self.data)

        auth = self.auth_owner
        auth['uuid'] = str(uuid4)

        force_authenticate(request, token=auth)

        response = view(request, news.id)
        self.assertEqual(response.status_code, 403)
