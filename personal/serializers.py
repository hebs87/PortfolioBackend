from rest_framework import serializers
from .models import *


class PersonalDetailsSerializer(serializers.ModelSerializer):
    """
    Serializes the PersonalDetails model and returns data as JSON
    """

    # TODO: Return name as field - join first and last name

    class Meta:
        model = PersonalDetails
        fields = ('id', 'first_name', 'last_name', 'job_title', 'email', 'phone', 'address', 'about')


class ProfessionalSkillsSerializer(serializers.ModelSerializer):
    """
    Serializes the ProfessionalSkills model and returns data as JSON
    """
    class Meta:
        model = PersonalDetails
        fields = ('id', 'skill', 'percentage_completed')


class WorkExperienceSerializer(serializers.ModelSerializer):
    """
    Serializes the WorkExperience model and returns data as JSON
    """

    # TODO: Return from and to dates as formatted date strings (blank value should be 'Present')

    class Meta:
        model = PersonalDetails
        fields = ('id', 'company', 'date_from', 'date_to', 'job_title', 'description')


class EducationSerializer(serializers.ModelSerializer):
    """
    Serializes the Education model and returns data as JSON
    """

    # TODO: Return from and to dates as formatted date strings

    class Meta:
        model = PersonalDetails
        fields = ('id', 'title', 'qualification_type', 'date_from', 'date_to', 'awarding_body', 'grade', 'details')
