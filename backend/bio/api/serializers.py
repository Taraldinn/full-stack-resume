"""serializers for bio app models"""

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from bio.models import (
    Award,
    Education,
    ExtracurricularActivity,
    Profile,
    Project,
    Publication,
    Skill,
    SocialMediaLink,
    Testimonial,
    WorkExperience,
)


class ExtraCurriculumSerializer(serializers.ModelSerializer):
    """
    Docstring for ExtraCurriculumSerializer
    """

    class Meta:
        """
        Docstring for Meta
        """

        model = ExtracurricularActivity
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    """
    Docstring for EducationSerializer
    """

    class Meta:
        """
        Docstring for Meta
        """

        model = Education
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    """Docstring for ProjectSerializer"""

    class Meta:
        """Docstring for Meta"""

        model = Project
        fields = "__all__"


class PublicationSerializer(serializers.ModelSerializer):
    """Docstring for PublicationSerializer"""

    class Meta:
        """Docstring for Meta"""

        model = Publication
        fields = "__all__"


class AwardSerializer(serializers.ModelSerializer):
    """Docstring for AwardSerializer"""

    class Meta:
        """Docstring for Meta"""

        model = Award
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):
    """Docstring for TestimonialSerializer"""

    class Meta:
        """Docstring for Meta"""

        model = Testimonial
        fields = "__all__"


class WorkExperienceSerializer(serializers.ModelSerializer):
    """Docstring for WorkExperienceSerializer"""

    class Meta:
        """Docstring for Meta"""

        model = WorkExperience
        fields = "__all__"


class SocialMediaLinkSerializer(serializers.ModelSerializer):
    """Serializer for SocialMediaLink model"""

    class Meta:
        """Meta class for SocialMediaLinkSerializer"""

        model = SocialMediaLink
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    """Serializer for Skill model"""

    class Meta:
        """Meta class for SkillSerializer"""

        model = Skill
        fields = "__all__"


class ProfileListSerializer(serializers.ModelSerializer):
    """Serializer for listing profiles"""

    url = serializers.HyperlinkedIdentityField(
        view_name="profile-detail", lookup_field="username"
    )

    class Meta:
        """Meta class for ProfileListSerializer"""

        model = Profile
        fields = ["id", "username", "url"]


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for Profile model"""

    educations = EducationSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    publications = PublicationSerializer(many=True, read_only=True)
    awards = AwardSerializer(many=True, read_only=True)
    testimonials = TestimonialSerializer(many=True, read_only=True)
    extracurricular_activities = ExtraCurriculumSerializer(many=True, read_only=True)
    work_experiences = WorkExperienceSerializer(many=True, read_only=True)
    social_media_links = SocialMediaLinkSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        """Meta class for ProfileSerializer"""

        model = Profile
        exclude = [
            "password",  # User password hash
            "email",  # Personal email address
            "is_staff",  # Admin privileges
            "is_superuser",  # Superuser privileges
            "user_permissions",  # User permissions
            "groups",  # User
        ]


class UserRegistrationSerializers(serializers.ModelSerializer):
    """Serializer for user registration"""

    password = serializers.CharField(write_only=True, min_length=8, max_length=128)
    password_confirm = serializers.CharField(
        write_only=True, min_length=8, max_length=128
    )

    class Meta:
        """Meta class for UserRegistrationSerializers"""

        model = Profile
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password_confirm",
        ]

    def validate(self, attrs):
        """Validate user registration data"""
        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError("Passwords do not match.")
        try:
            validate_password(attrs["password"])
        except ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return attrs

    def create(self, validated_data):
        """Create a new user"""
        validated_data.pop("password_confirm")
        password = validated_data.pop("password")
        user = Profile.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
