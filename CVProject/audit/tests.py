from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

from .models import RequestLog

class LoggingMiddlewareTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_logging_middleware_creates_log(self):
        # Ensure no logs exist
        self.assertEqual(RequestLog.objects.count(), 0)

        # Perform GET request to a tracked URL
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        # Check that a log was created
        self.assertEqual(RequestLog.objects.count(), 1)
        log = RequestLog.objects.first()
        self.assertEqual(log.HTTP_method, "GET")
        self.assertEqual(log.path, reverse('home'))
        self.assertEqual(log.query_string, "")
        self.assertIn(log.remote_IP, ["127.0.0.1", "::1"])

    def test_logging_middleware_with_authenticated_user(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        log = RequestLog.objects.first()
        self.assertIsNotNone(log.logged_user)
        self.assertEqual(log.logged_user.username, 'testuser')

class RecentLogsViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_recent_logs_view_shows_latest_10(self):
        for i in range(12):
            RequestLog.objects.create(
                HTTP_method='GET',
                path=f'/test-path-{i}/',
                query_string='',
                remote_IP='127.0.0.1',
                timestamp=timezone.now()
            )
        response = self.client.get(reverse('logs'))
        self.assertEqual(response.status_code, 200)

        # Check context logs
        logs = response.context['logs']
        self.assertEqual(len(logs), 10)

        # Ensure logs are ordered by timestamp descending
        paths = [log.path for log in logs]
        expected_paths = [f'/test-path-{i}/' for i in reversed(range(2, 12))]
        self.assertEqual(paths, expected_paths)

    def test_recent_logs_view_no_logs(self):
        response = self.client.get(reverse('logs'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['logs']), [])
