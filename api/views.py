from rest_framework import generics
from post.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticated, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class PostUserWritePermission(BasePermission):
    message = 'Editing post is restricted to author only'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)
        
    #Custom Query Set 
    def get_queryset(self):
        return Post.objects.all()
            





# """ class PostList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class EventList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = EventSerializer


# class EventDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = EventSerializer """