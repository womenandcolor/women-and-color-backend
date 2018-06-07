# Django
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model

# App
from wac.apps.accounts.models import (Profile, ImageUpload, FeaturedTalk)
from wac.apps.core.models import Topic
from wac.apps.core.api.serializers import TopicSerializer

# Rest framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class FeaturedTalkSerializer(serializers.ModelSerializer):
    class Meta():
        model = FeaturedTalk
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=False)
    featured_talks = FeaturedTalkSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ProfileSerializer, self).to_representation(instance)
        data['display_name'] = instance.display_name()
        if instance.location is not None:
            data['city'] = instance.location.city
        return data

    def update(self, instance, validated_data):
        topics_data = validated_data.pop('topics')
        instance = super(ProfileSerializer, self).update(instance, validated_data)

        instance.topics.clear()

        for topic_data in topics_data:
            topic_qs = Topic.objects.filter(topic__iexact=topic_data['topic'])

            if topic_qs.exists():
                topic = topic_qs.first()

            instance.topics.add(topic)

        return instance


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(
        read_only=True
    )

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=6)

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'],
            validated_data['email'],
            validated_data['password']
        )

        request = self.context.get('request')
        data = request.data

        user.save()

        auth_user = authenticate(
            username=validated_data['email'],
            password=validated_data['password']
        )
        login(self.context.get('request'), auth_user)
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'profile')


class ImageSerializer(serializers.ModelSerializer):
    class Meta():
        model = ImageUpload
        fields = ('file', 'profile')