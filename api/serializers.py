from rest_framework import serializers
from post.models import Post, Event


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'category', 'author', 'slug', 'status', 'country', 'assignment',
        'location', 'client_name', 'start_date', 'completion_date', 'amount_of_project',
        'duration', 'worker', 'officer', 'description_of_project', 'service_description')
        


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'desc', 'image')
        model = Event

