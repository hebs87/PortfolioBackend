from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Projects, Messages
from .serializers import ProjectsSerializer, MessagesSerializer


# Create your views here.
class ProjectsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A read only viewset to return Projects model objects to the frontend
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class MessagesViewSet(viewsets.ModelViewSet):
    """
    A viewset to save the contact form data to the Messages model
    Once saved, an email is sent to me and the user
    """
    # TODO: Overwrite list method to render Django template

    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer

    @action(detail=True, methodss=['post'])
    def send_emails(self, request):
        """
        Send relevant emails on successful form submission
        """
        try:
            messages = Messages()
            messages.send_contact_submitted_email(request.data)
            messages.send_confirmation_email(request.data)
            return Response({'message': 'emails sent'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'failed to send emails'}, status=status.HTTP_400_BAD_REQUEST)
