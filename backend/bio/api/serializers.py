from rest_framework import serializers
from bio.models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
          # Start with all fields to see what's available
        read_only_fields = ['id', 'date_joined', 'last_login']



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


# Models => Serializer => Views => urls.py
# Models =>
# Serializer = skeleton for the data structure
# Views = logic to handle requests and responses