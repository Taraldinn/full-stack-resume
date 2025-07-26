from rest_framework import generics
from bio.api.serializers import *
from bio.models import Profile, Education
from rest_framework import permissions, viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]



class EducationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows education records to be viewed or edited.
    """
    queryset = Education.objects.all()  # Adjust this to your actual Education model
    serializer_class = EducationSerializer  # Adjust this to your actual Education serializer
    permission_classes = [permissions.IsAuthenticated]






