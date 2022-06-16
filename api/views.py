from email import message
from rest_framework import generics
from post.models import Post, Event
from .serializers import PostSerializer, EventSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions, BasePermission

class PostUserWritePermission(BasePermission):
    message = 'Editing post is restricted to author only'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
            


class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EventList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Post.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = EventSerializer