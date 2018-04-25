# App
from wac.apps.core.api.serializers import LocationSerializer, TopicSerializer
from wac.apps.core.models import Location, Topic
from wac.apps.accounts.models import Profile

# Rest Framework
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    @list_route(methods=['get'])
    def active(self, request, *args, **kwargs):
        unique_user_locations = Profile.objects.filter(status=Profile.APPROVED).values_list('location', flat=True).distinct()
        user_location_ids = list(filter(None.__ne__, unique_user_locations))
        queryset = Location.objects.filter(pk__in=user_location_ids)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    http_method_names = ['get', 'post']

    def get_queryset(self):
        queryset = Topic.objects.all()

        q = self.request.query_params.get('q', None)
        if q is not None:
            queryset = queryset.filter(topic__icontains=q)

        return queryset
