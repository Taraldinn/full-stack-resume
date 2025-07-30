from rest_framework import generics
from bio.api.serializers import *
from bio.models import Profile, Education
from rest_framework import permissions, viewsets

from rest_framework.generics import RetrieveAPIView
from bio.models import Profile
from bio.api.serializers import ProfileSerializer

class UserProfileView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'username'



