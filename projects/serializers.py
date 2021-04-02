from rest_framework import serializers
from .models import *


class ProjectsSerializer(serializers.ModelSerializer):
    """
    Serializes the Projects model and returns data as JSON
    """
    class Meta:
        model = Projects
        fields = ('id', 'name', 'description', 'image', 'link')


class MessagesSerializer(serializers.ModelSerializer):
    """
    Serializes the Messages model and returns data as JSON
    """
    created_string = serializers.SerializerMethodField()

    def get_created_string(self, obj):
        return obj.created.strftime("%d %b %Y")

    class Meta:
        model = Messages
        fields = ('id', 'created_string', 'name', 'subject', 'email', 'message')
