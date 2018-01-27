# Django
from django.contrib.auth.models import User

# App
from wac.apps.account.api.serializers import UserSerializer

# Rest Framework
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
