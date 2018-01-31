# App
from wac.apps.core.api.serializers import LocationSerializer
from wac.apps.core.models import Location

# Rest Framework
from rest_framework import viewsets


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
