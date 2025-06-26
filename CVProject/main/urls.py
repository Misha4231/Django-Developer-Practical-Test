from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import home, cv, render_cv_pdf, CVViewSet

router = DefaultRouter()
router.register('cv', CVViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('cv/<int:id>/', cv, name='cv'),
    path('cv/<int:id>/pdf', render_cv_pdf, name='cv-pdf'),
    path('api/', include(router.urls)),
]