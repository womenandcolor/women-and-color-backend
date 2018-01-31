# Django
from django.contrib.auth.models import User

# App
from wac.apps.account.api.serializers import (
    UserSerializer,
    ProfileSerializer
)
from wac.apps.account.models import Profile

# Rest Framework
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
