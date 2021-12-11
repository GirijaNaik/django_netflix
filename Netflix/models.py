from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids')
)

MOVIE_CHOICES = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single')
)

# Create your models here.
class CustomUser(AbstractUser):
    profile = models.TextField(max_length=200)

class Profile(models.Model):
    name = models.CharField(max_length=300)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4)

class movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.CharField(max_length=300)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(max_length=100, choices=MOVIE_CHOICES)
    flyer = models.ImageField(upload_to='flyers')
    age_limit = models.CharField(max_length=100, choices=AGE_CHOICES)

class video(models.Model):
    file = models.FileField(upload_to='movies')
