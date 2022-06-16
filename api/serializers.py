from rest_framework import serializers
from post.models import Post, Event


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'category', 'author', 'status', 'country', 'assignment',
        'location', 'client_name', 'start_date', 'completion_date', 'amount_of_project',
        'duration', 'worker', 'officer', 'description_of_project', 'service_description' )
        model = Post


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'desc', 'image')
        model = Event

