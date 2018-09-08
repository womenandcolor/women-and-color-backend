# App
from wac.apps.core.models import Location, Topic, SubscriptionGroup

# Rest framework
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class SubscriptionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionGroup
        fields = '__all__'
