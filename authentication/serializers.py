from django.contrib.auth.models import User
from rest_framework import serializers

from authentication.models import Profile


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = User


class ProfileSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        fields = ('user', 'posts')
        model = Profile
        read_only_fields = ('user',)
