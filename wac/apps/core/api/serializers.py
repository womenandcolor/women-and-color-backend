# App
from wac.apps.core.models import Location

# Rest framework
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
