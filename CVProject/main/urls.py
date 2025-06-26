from django.urls import path

from .views import home, cv

urlpatterns = [
    path('', home, name='home'),
    path('cv/<int:id>/', cv, name='cv')
]