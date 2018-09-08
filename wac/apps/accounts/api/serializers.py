# Django
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model
from django.conf import settings

# App
from wac.apps.accounts.models import (Profile, ImageUpload, FeaturedTalk)
from wac.apps.core.models import Topic, SubscriptionGroup
from wac.apps.core.api.serializers import TopicSerializer, SubscriptionGroupSerializer

# Rest framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class FeaturedTalkSerializer(serializers.ModelSerializer):
    class Meta():
        model = FeaturedTalk
        fields = '__all__'

    def to_representation(self, instance):
        data = super(FeaturedTalkSerializer, self).to_representation(instance)
        if instance.image is not None and settings.AWS_S3_CUSTOM_DOMAIN in instance.image:
            aws_domain, media_path = instance.image.split(settings.AWS_S3_CUSTOM_DOMAIN)
            data['image'] = "https://{}{}".format(settings.CLOUDFRONT_DOMAIN, media_path)
        return data


class ProfileSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=False)
    subscription_groups = SubscriptionGroupSerializer(many=True, read_only=False)
    featured_talks = FeaturedTalkSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ProfileSerializer, self).to_representation(instance)
        data['display_name'] = instance.display_name()
        if instance.image is not None and settings.AWS_S3_CUSTOM_DOMAIN in instance.image:
            aws_domain, media_path = instance.image.split(settings.AWS_S3_CUSTOM_DOMAIN)
            data['image'] = "https://{}{}".format(settings.CLOUDFRONT_DOMAIN, media_path)
        if instance.location is not None:
            data['city'] = instance.location.city
        return data

    def update(self, instance, validated_data):
        topics_data = validated_data.pop('topics')
        subscription_group_data = validated_data.pop('subscription_groups')
        instance = super(ProfileSerializer, self).update(instance, validated_data)

        instance.topics.clear()
        instance.subscription_groups.clear()

        for topic_data in topics_data:
            topic_qs = Topic.objects.filter(topic__iexact=topic_data['topic'])

            if topic_qs.exists():
                topic = topic_qs.first()

            instance.topics.add(topic)

        for group in subscription_group_data:
            group_qs = SubscriptionGroup.objects.filter(group_id__iexact=group['group_id'])

            if group_qs.exists():
                group_obj = group_qs.first()

            instance.subscription_groups.add(group_obj)

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

    def to_representation(self, instance):
        data = super(UserSerializer, self).to_representation(instance)
        del data['password']
        return data


class ImageSerializer(serializers.ModelSerializer):
    class Meta():
        model = ImageUpload
        fields = ('file', 'profile')

