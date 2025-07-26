from django.urls import include, path
from rest_framework import routers

from bio.api import views


router = routers.DefaultRouter()
router.register(r'profiles', views.UserViewSet)
router.register(r'educations', views.EducationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    ]