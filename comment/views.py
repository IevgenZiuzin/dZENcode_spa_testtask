from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from .models import Comment
from .serializers import UserCommentSerializer, RateCommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(parent=None).order_by('-datetime')
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            if self.action == 'rate':
                return RateCommentSerializer
        return UserCommentSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)

    @action(detail=True)
    def answers(self, request, pk=None):
        queryset = Comment.objects.filter(parent=pk).order_by('-datetime')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def rate(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        if comment.rated_users.filter(id=user.id).exists():
            return Response({'detail': 'Already rated this comment.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = RateCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment.rate += serializer.data['rate']
        comment.rated_users.add(user)
        comment.save()
        return Response(RateCommentSerializer(comment).data)
