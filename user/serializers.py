from djoser.serializers import UserCreateSerializer
from .models import AppUser


class AppUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = AppUser
        fields = ('email', 'password', 'username', 'home_page')