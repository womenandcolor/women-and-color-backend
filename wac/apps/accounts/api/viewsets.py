# Django
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector

# App
from wac.apps.accounts.api.serializers import (
    UserSerializer,
    ProfileSerializer,
    ImageSerializer
)
from wac.apps.accounts.models import (Profile, ProfileLocation, ImageUpload)

# Rest Framework
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put']

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return User.objects.none()
        return User.objects.filter(
            id=self.request.user.id
        ).all()


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        queryset = Profile.objects.all().order_by("-pk")

        location = self.request.query_params.get('location', None)
        if location is not None:
            queryset = queryset.filter(location=location)

        poc = self.request.query_params.get('poc', None)
        if poc is not None:
            queryset = queryset.filter(poc=True)

        woman = self.request.query_params.get('woman', None)
        if woman is not None:
            queryset = queryset.filter(woman=True)

        query = self.request.query_params.get('q', None)
        if query is not None:
            queryset = queryset.annotate(
                search =
                    SearchVector('first_name', 'last_name', 'description', 'organization', 'topics__topic')
            ).filter(search=query)

        if 'offset' in self.request.GET or 'limit' in self.request.GET:
            limit = int(self.request.query_params.get('limit', 20))
            offset = int(self.request.query_params.get('offset', 0))
            queryset = queryset[offset:offset+limit]

        return queryset


class ImageUploadViewSet(viewsets.ModelViewSet):

    queryset = ImageUpload.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        profile = Profile.objects.get(pk=int(self.request.data.get('profile')))
        file = self.request.data.get('file')
        serializer.save(profile=profile, file=file)
