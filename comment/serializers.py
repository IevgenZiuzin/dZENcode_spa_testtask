from collections import OrderedDict
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['rated_users']
        read_only_fields = ['id', 'user', 'datetime', 'rate']

    def to_representation(self, instance):
        result = super(CommentSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])


class RateCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'user', 'rate')
        read_only_fields = ('id', 'user')

    def validate_rate(self, value):
        if value not in [-1, 1]:
            raise serializers.ValidationError(detail=f'Rate value could be -1 or 1, not {value}', code=400)
        return value
