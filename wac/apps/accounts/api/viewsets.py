# Django
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector
from django.shortcuts import get_object_or_404

# App
from wac.apps.accounts.api.serializers import (
    UserSerializer,
    ProfileSerializer,
    ImageSerializer,
    FeaturedTalkSerializer
)
from wac.apps.accounts.models import (Profile, ProfileLocation, ImageUpload, FeaturedTalk)

# Rest Framework
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import permissions


class UpdatePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        submitted_id = request.data.get('id')
        if view.action == 'update' and submitted_id != request.user.id:
            return False
        return True

class ModifyFeaturedTalkPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        profile_id = request.data.get('profile')
        if view.action == 'create' and profile_id != request.user.id:
            return False
        if view.action == 'update' and profile_id != request.user.id:
            return False
        if view.action == 'destroy' and profile_id != request.user.id:
            return False
        return True


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put']
    permission_classes = (UpdatePermissions,)

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return User.objects.none()
        return User.objects.filter(
            id=self.request.user.id
        ).all()


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    http_method_names = ['get', 'post', 'put']
    permission_classes = (UpdatePermissions,)

    def get_queryset(self):
        queryset = Profile.objects.filter(status=Profile.APPROVED).order_by("-pk")

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

    def get_object(self):
        queryset = Profile.objects.all()

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj


class ImageUploadViewSet(viewsets.ModelViewSet):

    queryset = ImageUpload.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        profile = Profile.objects.get(pk=int(self.request.data.get('profile')))
        file = self.request.data.get('file')
        serializer.save(profile=profile, file=file)

class FeaturedTalkViewSet(viewsets.ModelViewSet):

    queryset = FeaturedTalk.objects.order_by('id').reverse()
    serializer_class = FeaturedTalkSerializer
    permission_classes = (ModifyFeaturedTalkPermissions,)
    http_method_names = ['get', 'post', 'put', 'delete']

    def perform_create(self, serializer):
        profile = Profile.objects.get(pk=int(self.request.data.get('profile')))

        serializer.save(profile=profile,
                        event_name=self.request.data.get('event_name'),
                        talk_title=self.request.data.get('talk_title'),
                        url=self.request.data.get('url'))
