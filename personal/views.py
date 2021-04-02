from rest_framework import viewsets
from .models import PersonalDetails, ProfessionalSkills, WorkExperience, Education
from .serializers import (
    PersonalDetailsSerializer, ProfessionalSkillsSerializer,
    WorkExperienceSerializer, EducationSerializer
)


# Create your views here.
class PersonalDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A read only viewset to return PersonalDetails model objects to the frontend
    Only return the first record, as that is the only record to be rendered in the frontend
    """
    queryset = PersonalDetails.objects.first()
    serializer_class = PersonalDetailsSerializer


class ProfessionalSkillsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A read only viewset to return ProfessionalSkills model objects to the frontend
    """
    queryset = ProfessionalSkills.objects.all()
    serializer_class = ProfessionalSkillsSerializer


class WorkExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A read only viewset to return WorkExperience model objects to the frontend
    Order by newest to oldest date_from
    """
    queryset = WorkExperience.objects.all().order_by('-date_from')
    serializer_class = WorkExperienceSerializer


class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A read only viewset to return Education model objects to the frontend
    Order by newest to oldest date_from
    """
    queryset = Education.objects.all().order_by('-date_from')
    serializer_class = EducationSerializer
