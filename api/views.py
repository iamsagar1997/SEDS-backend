from rest_framework import generics
from post.models import Post, Event
from .serializers import PostSerializer, EventSerializer


class PostList(generics.ListCreateAPIView):
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