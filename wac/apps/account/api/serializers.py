# Django
from django.contrib.auth.models import User

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

        if validated_data.get('first_name'):
            user.first_name = validated_data.get('first_name')

        if validated_data.get('last_name'):
            user.last_name = validated_data.get('last_name')

        user.save()

        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
