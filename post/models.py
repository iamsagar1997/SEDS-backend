from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=255)
    #excerpt = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    country = models.CharField(max_length=255,blank=True)
    assignment = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    completion_Date = models.DateTimeField(auto_now=True)
    amount_Of_project = models.CharField(max_length=255, null=True)
    duration = models.CharField(max_length=255, null=True,blank=True)
    worker = models.IntegerField()
    officer = models.CharField(max_length=255,blank=True)
    description_of_project = models.TextField()
    service_description = models.TextField()

    def __str__(self):
        return self.Title
    
