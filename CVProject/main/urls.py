from django.urls import path

from .views import home, cv, render_cv_pdf

urlpatterns = [
    path('', home, name='home'),
    path('cv/<int:id>/', cv, name='cv'),
    path('cv/<int:id>/pdf', render_cv_pdf, name='cv-pdf'),
]