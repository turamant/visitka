from django.utils import timezone
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

