from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import AppUser, GuestUser


class AppUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = AppUser
        fields = ('email', 'password', 'username', 'home_page')


class GuestUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuestUser
        fields = '__all__'

