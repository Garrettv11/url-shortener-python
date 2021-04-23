"""Restaurant app-level route registration"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.urlApp import views


router = DefaultRouter()
router.register("manager", views.ShortURLManagerViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("r/<short_path_component>", views.resolve_url)
]
