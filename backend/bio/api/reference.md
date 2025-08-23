"""
Docstring for bio.api.views

"""
```
- This is a module-level docstring. It should describe the purpose of the file, but currently it's empty.
---

```python
from django.forms import ValidationError
```
- Imports `ValidationError` from Django, used to raise validation errors in form or model logic.
---

```python
from rest_framework.authentication import get_user_model
```
- Imports `get_user_model` to get the custom user model if one is set, otherwise the default Django user.
---

```python
from rest_framework.decorators import action
```
- Imports the `action` decorator, which allows you to add custom endpoints to a ViewSet.
---

```python
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
```
- Imports permission classes. `IsAuthenticated` restricts access to authenticated users, `IsAuthenticatedOrReadOnly` allows read-only access for unauthenticated users.
---

```python
from rest_framework.response import Response
```
- Imports the `Response` class to return HTTP responses from API views.
---

```python
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
```
- Imports HTTP status codes for use in API responses.
---

```python
from rest_framework.viewsets import ModelViewSet
```
- Imports `ModelViewSet`, a DRF class that provides CRUD operations for a model.
---

```python
from bio.models import Profile
```
- Imports the `Profile` model from your app's models.
---

```python
from bio.api.serializers import (
    ProfileSerializer,
    ProfileListSerializer,
    UserRegistrationSerializers,
)
```
- Imports serializers for serializing/deserializing Profile data and user registration.
---

```python
User = get_user_model()
```
- Assigns the user model to `User` for use in the view.
---

```python
class ProfileViewSet(ModelViewSet):
    """
    Docstring for

    """
```
- Defines a viewset for the Profile model. The docstring is incomplete and should describe the class.
---

```python
    queryset = Profile.objects.all()
```
- Sets the default queryset for the viewset to all Profile objects.
---

```python
    lookup_field = "username"
```
- Tells DRF to use the `username` field for lookups (e.g., `/profiles/<username>/`).
---

```python
    permission_classes = [IsAuthenticatedOrReadOnly]
```
- Sets the default permissions: authenticated users can write, others can only read.
---

```python
    "Serializer class for the viewset"
```
- This is a stray string, likely meant to be a comment or docstring. It has no effect.
---

```python
    def get_serializer_class(self):
        if self.action == "list":
            return ProfileListSerializer
        elif self.action == "create_user":
            return UserRegistrationSerializers
        return ProfileSerializer
```
- Dynamically chooses which serializer to use based on the action (list, register, or default).
---

```python
    def get_permissions(self):
        if self.action == "create_user":
            permission_classes = []  # Anyone can register
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]

        return [permission() for permission in permission_classes]
```
- Dynamically sets permissions: registration is open, updates/deletes require authentication, others use default.
---

```python
    def get_queryset(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return Profile.objects.filter(username=self.request.user.username)
        return Profile.objects.all()
```
- Restricts update/delete actions to the current user's profile only; otherwise, returns all profiles.
---

```python
    def perform_update(self, serializer):
        # Ensure user can only update their own profile
        if serializer.instance.username != self.request.user.username:
            raise ValidationError("You can only update your own profile")
        serializer.save()
```
- Checks that the user is only updating their own profile; raises error if not.
---

```python
    def perform_destroy(self, instance):
        # Ensure user can only delete their own profile
        if instance.username != self.request.user.username:
            raise ValidationError("You can only delete your own profile")
        instance.delete()
```
- Checks that the user is only deleting their own profile; raises error if not.
---

```python
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
```
- Custom endpoint for user registration. Validates and saves the user, returns appropriate response.
---

```python
    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        """
        Get current user's profile
        """
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
```
- Custom endpoint to get the current user's profile. Only accessible to authenticated users.
---

**Summary:**  
This file defines a DRF `ModelViewSet` for user profiles, with custom registration and "me" endpoints, dynamic permissions, and logic to ensure users can only modify their own profiles. Each import and method is chosen to provide secure, RESTful access to profile data.# filepath: /home/aldinn/Documents/code/full stack projects/personal-portfolio/backend/bio/api/views.py

"""
Docstring for bio.api.views

"""
```
- This is a module-level docstring. It should describe the purpose of the file, but currently it's empty.
---

```python
from django.forms import ValidationError
```
- Imports `ValidationError` from Django, used to raise validation errors in form or model logic.
---

```python
from rest_framework.authentication import get_user_model
```
- Imports `get_user_model` to get the custom user model if one is set, otherwise the default Django user.
---

```python
from rest_framework.decorators import action
```
- Imports the `action` decorator, which allows you to add custom endpoints to a ViewSet.
---

```python
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
```
- Imports permission classes. `IsAuthenticated` restricts access to authenticated users, `IsAuthenticatedOrReadOnly` allows read-only access for unauthenticated users.
---

```python
from rest_framework.response import Response
```
- Imports the `Response` class to return HTTP responses from API views.
---

```python
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
```
- Imports HTTP status codes for use in API responses.
---

```python
from rest_framework.viewsets import ModelViewSet
```
- Imports `ModelViewSet`, a DRF class that provides CRUD operations for a model.
---

```python
from bio.models import Profile
```
- Imports the `Profile` model from your app's models.
---

```python
from bio.api.serializers import (
    ProfileSerializer,
    ProfileListSerializer,
    UserRegistrationSerializers,
)
```
- Imports serializers for serializing/deserializing Profile data and user registration.
---

```python
User = get_user_model()
```
- Assigns the user model to `User` for use in the view.
---

```python
class ProfileViewSet(ModelViewSet):
    """
    Docstring for

    """
```
- Defines a viewset for the Profile model. The docstring is incomplete and should describe the class.
---

```python
    queryset = Profile.objects.all()
```
- Sets the default queryset for the viewset to all Profile objects.
---

```python
    lookup_field = "username"
```
- Tells DRF to use the `username` field for lookups (e.g., `/profiles/<username>/`).
---

```python
    permission_classes = [IsAuthenticatedOrReadOnly]
```
- Sets the default permissions: authenticated users can write, others can only read.
---

```python
    "Serializer class for the viewset"
```
- This is a stray string, likely meant to be a comment or docstring. It has no effect.
---

```python
    def get_serializer_class(self):
        if self.action == "list":
            return ProfileListSerializer
        elif self.action == "create_user":
            return UserRegistrationSerializers
        return ProfileSerializer
```
- Dynamically chooses which serializer to use based on the action (list, register, or default).
---

```python
    def get_permissions(self):
        if self.action == "create_user":
            permission_classes = []  # Anyone can register
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]

        return [permission() for permission in permission_classes]
```
- Dynamically sets permissions: registration is open, updates/deletes require authentication, others use default.
---

```python
    def get_queryset(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return Profile.objects.filter(username=self.request.user.username)
        return Profile.objects.all()
```
- Restricts update/delete actions to the current user's profile only; otherwise, returns all profiles.
---

```python
    def perform_update(self, serializer):
        # Ensure user can only update their own profile
        if serializer.instance.username != self.request.user.username:
            raise ValidationError("You can only update your own profile")
        serializer.save()
```
- Checks that the user is only updating their own profile; raises error if not.
---

```python
    def perform_destroy(self, instance):
        # Ensure user can only delete their own profile
        if instance.username != self.request.user.username:
            raise ValidationError("You can only delete your own profile")
        instance.delete()
```
- Checks that the user is only deleting their own profile; raises error if not.
---

```python
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
```
- Custom endpoint for user registration. Validates and saves the user, returns appropriate response.
---

```python
    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        """
        Get current user's profile
        """
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
```
- Custom endpoint to get the current user's profile. Only accessible to authenticated users.
---

**Summary:**  
This file defines a DRF `ModelViewSet` for user profiles, with custom registration and "me" endpoints, dynamic permissions, and logic to ensure users can only modify their own profiles. Each import and method is chosen to provide secure, RESTful access to profile