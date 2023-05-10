from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import AppUser


class AppUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = AppUser
        fields = ('email', 'password', 'username', 'home_page')


class GuestCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)

    class Meta:
        fields = '__all__'

