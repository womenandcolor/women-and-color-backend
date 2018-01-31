# Django
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# App
from wac.apps.account.models import Profile

# Rest framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
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

        profile = data.get('profile')

        if profile:
            if profile.get('firstName'):
                user.first_name = profile.get('firstName')

            if profile.get('lastName'):
                user.last_name = profile.get('lastName')

        user.save()

        auth_user = authenticate(validated_data['email'], password=validated_data['password'])

        # login(self.context.get('request'), auth_user)
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ProfileSerializer, self).to_representation(instance)
        data['firstName'] = instance.user.first_name
        data['lastName'] = instance.user.last_name
        return data
