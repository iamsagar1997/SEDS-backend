from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=255, null=True, blank=False)
    desc  = models.TextField(blank=False)
    image = models.ImageField(null=True, upload_to='event')
    
    def __str__(self):
        return self.title 



class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    status = models.CharField(max_length=10, choices=options, default='published')
    slug = models.SlugField(max_length=250, unique_for_date='published')
    country = models.CharField(max_length=255,blank=True)
    assignment = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    completion_date = models.DateTimeField(default=timezone.now)
    amount_of_project = models.CharField(max_length=255, null=True)
    duration = models.CharField(max_length=255, null=True,blank=True)
    worker = models.IntegerField()
    officer = models.CharField(max_length=255,blank=True)
    description_of_project = models.TextField()
    service_description = models.TextField()
    objects = models.Manager()  
    postobjects = PostObjects()

    def __str__(self):
        return self.Title
    
