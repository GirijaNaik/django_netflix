from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids')
)

MOVIE_TYPE = (
    ('single', 'Single'),
    ('seasonal', 'Seasonal')
)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile')


class Profile(models.Model):
    name = models.CharField(max_length=225)
    age_limit = models.CharField(max_length=5, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)


    def __str__(self):
        return self.name +" "+self.age_limit

class Movie(models.Model):
    title: str = models.CharField(max_length=225)
    description: str = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    type = models.CharField(max_length=10, choices=MOVIE_TYPE)
    videos = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers', blank=True, null=True)
    age_limit = models.CharField(max_length=5, choices=AGE_CHOICES, blank=True, null=True)
    
class Upcoming_movie(models.Model):
    title: str = models.CharField(max_length=225)
    description: str = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=MOVIE_TYPE)
    flyer = models.ImageField(upload_to='flyers')
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    genre = models.CharField(max_length=200, db_index=True)
    age_limit = models.CharField(max_length=5, choices=AGE_CHOICES)

class Top_rated(models.Model):
    title: str = models.CharField(max_length=225)
    description: str = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=MOVIE_TYPE)
    flyer = models.ImageField(upload_to='flyers')
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    genre = models.CharField(max_length=200, db_index=True)
    age_limit = models.CharField(max_length=5, choices=AGE_CHOICES)

class comedy_movies(models.Model):
    title: str = models.CharField(max_length=225)
    description: str = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=MOVIE_TYPE)
    flyer = models.ImageField(upload_to='flyers')
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    genre = models.CharField(max_length=200, db_index=True)
    age_limit = models.CharField(max_length=5, choices=AGE_CHOICES)

class romantic_movies(models.Model):
    title: str = models.CharField(max_length=225)
    description: str = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=MOVIE_TYPE)
    flyer = models.ImageField(upload_to='flyers')
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    genre = models.CharField(max_length=200, db_index=True)
    age_limit = models.CharField(max_length=5, choices=AGE_CHOICES)


class action_movies(models.Model):
    title: str = models.CharField(max_length=225)
    description: str = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=MOVIE_TYPE)
    flyer = models.ImageField(upload_to='flyers')
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    genre = models.CharField(max_length=200, db_index=True)
    age_limit = models.CharField(max_length=5, choices=AGE_CHOICES)

class horror_movies(models.Model):
    title: str = models.CharField(max_length=225)
    description: str = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=MOVIE_TYPE)
    flyer = models.ImageField(upload_to='flyers')
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    genre = models.CharField(max_length=200, db_index=True)
    age_limit = models.CharField(max_length=5, choices=AGE_CHOICES)

class kids_movies(models.Model):
    title: str = models.CharField(max_length=225)
    description: str = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=MOVIE_TYPE)
    flyer = models.ImageField(upload_to='flyers')
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    genre = models.CharField(max_length=200, db_index=True)
    age_limit = models.CharField(max_length=5, choices=AGE_CHOICES)


class Video(models.Model):
    title: str = models.CharField(max_length=225, blank=True, null=True)
    file = models.FileField(upload_to='movies')
