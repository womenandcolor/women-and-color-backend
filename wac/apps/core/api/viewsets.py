# App
from wac.apps.core.api.serializers import LocationSerializer, TopicSerializer
from wac.apps.core.models import Location, Topic

# Rest Framework
from rest_framework import viewsets


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    http_method_names = ['get', 'post']

    def get_queryset(self):
        queryset = Topic.objects.all()

        q = self.request.query_params.get('q', None)
        if q is not None:
            queryset = queryset.filter(topic__icontains=q)

        return queryset
