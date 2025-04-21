# TODO:  Напишите свой вариант
from .serializers import PostSerializer, CommentSerializer, GroupSerializer
from rest_framework import viewsets
from posts.models import Post, Comment, Group
from .permissions import OwnerOrReadOnly
from django.shortcuts import get_object_or_404

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = None

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly, )
    
    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def get_queryset(self):
        comments = self.get_post().comments.all()
        return comments
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.get_post().id)

    