from rest_framework import serializers
from django.contrib.auth.models import User
from bio.models import Profile


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'phone_number', 'address', 'date_of_birth', 'bio']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"