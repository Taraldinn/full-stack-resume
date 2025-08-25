"""
Docstring for bio.urls
"""

from rest_framework.routers import DefaultRouter
from django.urls import include, path
from bio.api.views import ProfileViewSet

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet, basename="profile")

urlpatterns = [
    path("", include(router.urls)),
]
