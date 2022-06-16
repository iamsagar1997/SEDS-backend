from rest_framework import generics
from post.models import Post, Event
from .serializers import PostSerializer, EventSerializer
from rest_framework.permissions import IsAdminUser

class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = EventSerializer