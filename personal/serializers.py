from rest_framework import serializers
from .models import *


class PersonalDetailsSerializer(serializers.ModelSerializer):
    """
    Serializes the PersonalDetails model and returns data as JSON
    """
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        """
        Return full name string
        """
        return f'{obj.first_name} {obj.last_name}'

    class Meta:
        model = PersonalDetails
        fields = ('id', 'name', 'job_title', 'email', 'phone', 'address', 'about')


class ProfessionalSkillsSerializer(serializers.ModelSerializer):
    """
    Serializes the ProfessionalSkills model and returns data as JSON
    """
    class Meta:
        model = ProfessionalSkills
        fields = ('id', 'skill', 'percentage_completed')


class WorkExperienceSerializer(serializers.ModelSerializer):
    """
    Serializes the WorkExperience model and returns data as JSON
    """
    date_from_string = serializers.SerializerMethodField()
    date_to_string = serializers.SerializerMethodField()

    def format_string(self, date_obj):
        """
        Convert date object to string
        """
        if date_obj:
            return date_obj.strftime("%b %Y")
        else:
            return 'Present'

    def get_date_from_string(self, obj):
        """
        Convert date_from to string
        """
        return self.format_string(obj.date_from)

    def get_date_to_string(self, obj):
        """
        Convert date_to to string
        """
        return self.format_string(obj.date_to)

    class Meta:
        model = WorkExperience
        fields = ('id', 'company', 'date_from_string', 'date_to_string', 'job_title', 'description')


class EducationSerializer(serializers.ModelSerializer):
    """
    Serializes the Education model and returns data as JSON
    """
    date_from_string = serializers.SerializerMethodField()
    date_to_string = serializers.SerializerMethodField()

    def format_string(self, date_obj):
        """
        Convert date object to year string
        """
        if date_obj:
            return date_obj.strftime("%Y")
        else:
            return ''

    def get_date_from_string(self, obj):
        """
        Convert date_from to string
        """
        return self.format_string(obj.date_from)

    def get_date_to_string(self, obj):
        """
        Convert date_to to string
        """
        return self.format_string(obj.date_to)

    class Meta:
        model = Education
        fields = ('id', 'title', 'qualification_type', 'date_from_string', 'date_to_string', 'awarding_body', 'grade', 'details')
