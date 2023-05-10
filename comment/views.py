from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from .models import Comment
from user.models import AppUser
from .serializers import UserCommentSerializer, GuestCommentSerializer, RateCommentSerializer
from user.serializers import AppUserCreateSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(parent=None).order_by('-datetime')

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            if self.action == 'rate':
                return RateCommentSerializer
            return UserCommentSerializer
        return GuestCommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        guest = serializer.data.get('guest')
        if guest:
            username = guest['username']
            serializer = AppUserCreateSerializer()
            AppUser.objects.create(username=username, guest=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response('some response')

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
