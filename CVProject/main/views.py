from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from .models import CV

def home(request: HttpRequest):
    cv_list = CV.objects.all()
    return render(request, 'home.html', {'cv_list': cv_list})

def cv(request: HttpRequest, id: int):
    cv = get_object_or_404(CV, pk=id)
    return render(request, 'detail.html', {'cv': cv})