from django.urls import reverse

from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate, APIClient

from uuid import uuid4


from .views import CommentsStatsView, NewsStatsView, RSSParserStatsView, UsersStatView


class IntegrationTestCase(APITestCase):
    def setUp(self):
        self.urls = ['stats-comments', 'stats-news',
                     'stats-rss-parser', 'stats-users']

        self.views = [CommentsStatsView.as_view(), NewsStatsView.as_view(),
                      RSSParserStatsView.as_view(), UsersStatView.as_view()]

        self.factory = APIRequestFactory()

        self.auth = {'uuid': uuid4(), 'username': 'username',
                     'token': 'token', 'is_staff': False}

        self.initialdata = {
            'user': uuid4(),
            'action': '',
            'input': {'data': 'data'},
            'output': {'data': 'data'}
        }

    def test_stats_post_actions_are_valid(self, format='json'):
        actions = ['PUT', 'POST', 'DELETE', 'PATCH', 'GET']
        
        msg = 'For view {view} and action {action} received code {code}'
        for view, url in zip(self.views, self.urls):
            for action in actions:
                data = self.initialdata
                data['action'] = action

                request = self.factory.post(reverse(url), data=data)
                force_authenticate(request, token=self.auth)

                response = view(request)
                self.assertEqual(response.status_code, 201, msg.format(
                    view=view, action=action, code=response.status_code
                ))

    def test_stats_post_action_are_invalid(self):
        actions = ['PUTS', 'POSTS', "GETS"]

        msg = 'For view {view} and action {action} received code {code}'
        for view, url in zip(self.views, self.urls):
            for action in actions:
                data = self.initialdata
                data['action'] = action

                request = self.factory.post(reverse(url), data=data)
                force_authenticate(request, token=self.auth)

                response = view(request)
                self.assertEqual(response.status_code, 400, msg.format(
                    view=view, action=action, code=response.status_code
                ))
