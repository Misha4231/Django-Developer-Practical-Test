from django.db import models
from django.contrib.auth.models import User

class RequestLog(models.Model):
    timestamp = models.DateTimeField()
    HTTP_method = models.CharField(max_length=10)
    path = models.CharField(max_length=2048)
    query_string = models.CharField(max_length=1024, blank=True)
    remote_IP = models.CharField(max_length=45)
    logged_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.timestamp} {self.HTTP_method} {self.path}"