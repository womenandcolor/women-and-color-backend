# Django
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# App
from wac.apps.accounts.models import Profile, ImageUpload

# Rest framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ProfileSerializer, self).to_representation(instance)
        data['display_name'] = instance.display_name()
        data['email'] = instance.user.email or instance.user.email
        data['image'] = 'data:image/jpeg;base64,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'
        return data


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
