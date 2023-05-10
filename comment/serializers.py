from rest_framework import serializers
from .models import Comment
from user.serializers import GuestCreateSerializer


class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id', 'datetime', 'rate', 'rated_users')


class GuestCommentSerializer(serializers.ModelSerializer):
    guest = GuestCreateSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'parent', 'content', 'datetime', 'rate', 'rated_users', 'guest')
        read_only_fields = ('id', 'datetime', 'rate', 'rated_users')


class RateCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'user', 'rate')
        read_only_fields = ('id', 'user')

    def validate_rate(self, value):
        if value not in [-1, 1]:
            raise serializers.ValidationError(detail=f'Rate value could be -1 or 1, not {value}', code=400)
        return value
