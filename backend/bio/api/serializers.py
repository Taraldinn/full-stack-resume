from rest_framework import serializers
from bio.models import *


class ExtraCurriculumSerializer(serializers.Serializer):
     class Meta:
         model = ExtracurricularActivity
         fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
    fields = '__all__'
class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'
class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = workExperience
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    publications = PublicationSerializer(many=True, read_only=True)
    awards = AwardSerializer(many=True, read_only=True)
    testimonials = TestimonialSerializer(many=True, read_only=True)
    extracurricular_activities = ExtraCurriculumSerializer(many=True, read_only=True)
    work_experiences= WorkExperienceSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'
          # Start with all fields to see what's available
        read_only_fields = ['id', 'date_joined', 'last_login']






# Models => Serializer => Views => urls.py
# Models =>
# Serializer = skeleton for the data structure
# Views = logic to handle requests and responses