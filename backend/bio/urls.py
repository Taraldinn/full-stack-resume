from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bio.api.views import UserProfileView

router = DefaultRouter()
router.register(r'users', UserProfileView)

urlpatterns = [
    path('', include(router.urls)),
]