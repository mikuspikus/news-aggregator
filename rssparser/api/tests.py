from django.urls import reverse

from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate, APIClient

from uuid import uuid4

from .views import FeedView, FeedsView, FeedParseView
from .models import Feed


class IntegrationTestCase(APITestCase):
    def setUp(self):
        self.feeds = 'feeds', FeedsView.as_view()
        self.feed = 'feed', FeedView.as_view()
        self.feed_parse = 'feed-parse', FeedParseView.as_view()

        self.factory = APIRequestFactory()

        self.owner = uuid4()

        self.auth_owner = {'uuid': str(self.owner), 'username': 'username',
                           'token': 'token', 'is_staff': False}

        self.data = {
            'user': self.owner,
            'name': 'How to unit test permissions in django-rest-framework?',
            'url': 'https://stackoverflow.com/questions/33607701/django-test-doesnt-populate-request-auth'
        }

    def test_post_new_feed(self):
        url, view = self.feeds
        request = self.factory.post(url, self.data)
        force_authenticate(request, token=self.auth_owner)

        response = view(request)

        self.assertEqual(response.status_code, 201)

    def test_patch_feed_by_owner(self):
        feed = Feed.objects.create(**self.data)

        url, view = self.feed
        request = self.factory.patch(url + '/' + str(feed.id), self.data)

        force_authenticate(request, token=self.auth_owner)

        response = view(request, feed.id)
        self.assertEqual(response.status_code, 202)

    def test_patch_feed_by_not_owner(self):
        feed = Feed.objects.create(**self.data)

        url, view = self.feed
        request = self.factory.patch(url + '/' + str(feed.id), self.data)

        auth = self.auth_owner
        auth['uuid'] = str(uuid4)

        force_authenticate(request, token=auth)

        response = view(request, feed.id)
        self.assertEqual(response.status_code, 403)
