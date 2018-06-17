# Rest Framework
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# App
from wac.apps.contact_speaker.api.serializers import ContactFormSerializer

class ContactFormViewSet(viewsets.ModelViewSet):
    serializer_class = ContactFormSerializer
    http_method_names = ['post']
    permission_classes = (AllowAny,)