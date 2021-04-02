from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('details', PersonalDetailsViewSet)
router.register('skills', ProfessionalSkillsViewSet)
router.register('experience', WorkExperienceViewSet)
router.register('education', EducationViewSet)

urlpatterns = [
    path('', include(router.urls))
]
