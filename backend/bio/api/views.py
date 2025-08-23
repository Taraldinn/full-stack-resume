"""
Docstring for bio.api.views

"""

from django.forms import ValidationError
from rest_framework.authentication import get_user_model
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet
from bio.models import Profile
from bio.api.serializers import (
    ProfileSerializer,
    ProfileListSerializer,
    UserRegistrationSerializers,
)

User = get_user_model()


class ProfileViewSet(ModelViewSet):
    """
    Docstring for

    """

    queryset = Profile.objects.all()
    lookup_field = "username"
    permission_classes = [IsAuthenticatedOrReadOnly]

    "this get_serializer_class function define that which serializer to use based on the action"

    def get_serializer_class(self):
        if self.action == "list":
            return ProfileListSerializer
        elif self.action == "create_user":
            return UserRegistrationSerializers
        return ProfileSerializer

    def get_permissions(self):
        if self.action == "create_user":
            permission_classes = []  # Anyone can register
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return Profile.objects.filter(username=self.request.user.username)
        return Profile.objects.all()

    def perform_update(self, serializer):
        # Ensure user can only update their own profile
        if serializer.instance.username != self.request.user.username:
            raise ValidationError("You can only update your own profile")
        serializer.save()

    def perform_destroy(self, instance):
        # Ensure user can only delete their own profile
        if instance.username != self.request.user.username:
            raise ValidationError("You can only delete your own profile")
        instance.delete()

    @action(detail=False, methods=["post"], url_path="register")
    def create_user(self, request):
        """
        Create a new user account - only one profile per user
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                return Response(
                    {"message": "User created successfully", "username": user.username},
                    status=HTTP_201_CREATED,
                )
            except ValueError as e:
                return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        """
        Get current user's profile
        """
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
