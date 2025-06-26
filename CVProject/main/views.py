from django.shortcuts import render
from django.http import HttpRequest

from .models import CV

def home(request: HttpRequest):
    cv_list = CV.objects.all()
    return render(request, 'home.html', {'cv_list': cv_list})