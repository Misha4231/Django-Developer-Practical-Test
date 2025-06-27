from django.utils import timezone
from django.http import HttpRequest
from ipware import get_client_ip

from .models import RequestLog


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)

        # Skip unneeded requests
        if request.path.startswith('/static/') or request.path.startswith('/admin/') or request.path.startswith('/favicon.ico'):
            return response

        RequestLog.objects.create(
            timestamp = timezone.now(),
            HTTP_method=request.method,
            path=request.path,
            query_string=request.META.get('QUERY_STRING', ''),
            remote_IP=get_client_ip(request)[0],
            logged_user=request.user if request.user.is_authenticated else None
        )

        return response