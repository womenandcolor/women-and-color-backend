from django.conf.urls import url

# App
from wac.apps.contact_speaker.api.serializers import ContactFormSerializer

# Rest framework

from rest_framework.generics import CreateAPIView


app_name="contact_speaker"

urlpatterns = [
  url(r'^contact_form/$', CreateAPIView.as_view(serializer_class=ContactFormSerializer), name='contact_speaker-list')
]
