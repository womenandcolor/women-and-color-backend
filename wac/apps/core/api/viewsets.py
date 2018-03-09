# App
from wac.apps.core.api.serializers import LocationSerializer, TopicSerializer
from wac.apps.core.models import Location, Topic

# Rest Framework
from rest_framework import viewsets


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
