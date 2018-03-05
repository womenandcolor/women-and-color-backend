# App
from wac.apps.contact_speaker.models import ContactForm

# Rest framework
from rest_framework import serializers


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'