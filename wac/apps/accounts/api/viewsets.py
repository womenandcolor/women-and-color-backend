# Django
from django.contrib.auth.models import User

# App
from wac.apps.accounts.api.serializers import (
    UserSerializer,
    ProfileSerializer
)
from wac.apps.accounts.models import Profile

# Rest Framework
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put']

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return User.objects.none()
        return User.objects.filter(
            id=self.request.user.id
        ).all()


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    http_method_names = ['get', 'put']

    def get_queryset(self):
        return Profile.objects.all().order_by("-pk")
