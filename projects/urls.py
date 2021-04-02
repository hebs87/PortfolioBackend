from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('details', ProjectsViewSet)
router.register('messages', MessagesViewSet)

urlpatterns = [
    path('', include(router.urls))
]
