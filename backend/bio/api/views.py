from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import permissions, viewsets

from bio.api.serializers import UserSerializer
from bio.models import Profile


class UserProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return the current user's profile
        return Profile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)