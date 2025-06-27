from django.shortcuts import render
from django.http import HttpRequest

from .models import RequestLog

def recent_logs(request: HttpRequest):
    logs = RequestLog.objects.all().order_by('-timestamp')[:10]
    return render(request, 'logs.html', {'logs': logs})