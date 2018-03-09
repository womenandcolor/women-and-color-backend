# App
from wac.apps.core.api.serializers import LocationSerializer, TopicSerializer
from wac.apps.core.models import Location, Topic

# Rest Framework
from rest_framework import viewsets
from rest_framework.response import Response


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def list(self, request):
        queryset = Topic.objects.all()

        if 'q' in request.GET:
            q = request.GET.get('q')
            queryset = queryset.filter(topic__icontains=q)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
