from rest_framework import status, viewsets
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
    queryset = Messages.objects.all().order_by('-created')
    serializer_class = MessagesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        try:
            messages = Messages()
            messages.send_contact_submitted_email(request.data)
            messages.send_confirmation_email(request.data)
        except:
            return Response({'message': 'failed to send emails'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
