from django.urls import path

from .views import recent_logs

urlpatterns = [
    path('', recent_logs, name='logs')
]