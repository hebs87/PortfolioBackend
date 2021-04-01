from rest_framework import viewsets
from .models import Projects, Messages
from .serializers import ProjectsSerializer, MessagesSerializer


# Create your views here.
class ProjectsViewSet(viewsets.ModelViewSet):
    """
    A viewset to return Projects model objects to the frontend
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class MessagesViewSet(viewsets.ModelViewSet):
    """
    A viewset to save the messages from the contact form to the Messages model
    Once saved, an email is sent to me and also the user who completed the contact form
    """
    # TODO:
    #   - Send email functionality - to me and end user
    #   - Save record

    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
