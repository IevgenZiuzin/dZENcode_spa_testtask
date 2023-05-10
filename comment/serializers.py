from collections import OrderedDict
from rest_framework import serializers
from .models import Comment
from user.serializers import GuestUserSerializer


class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'parent', 'datetime', 'content', 'rate']
        read_only_fields = ['id', 'user', 'datetime', 'rate', 'rated_users']

    def to_representation(self, instance):
        result = super(UserCommentSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])


class GuestCommentSerializer(UserCommentSerializer):
    guest = GuestUserSerializer()

    class Meta(UserCommentSerializer.Meta):
        fields = ['id', 'guest', 'parent', 'datetime', 'content', 'rate']


class RateCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'user', 'rate')
        read_only_fields = ('id', 'user')

    def validate_rate(self, value):
        if value not in [-1, 1]:
            raise serializers.ValidationError(detail=f'Rate value could be -1 or 1, not {value}', code=400)
        return value
