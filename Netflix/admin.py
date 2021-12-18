from django.contrib import admin
from .models import CustomUser, Movie, Profile, Video, Upcoming_movie, Top_rated, comedy_movies, romantic_movies, action_movies, horror_movies, kids_movies

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Movie)
admin.site.register(Upcoming_movie)
admin.site.register(Top_rated)
admin.site.register(comedy_movies)
admin.site.register(romantic_movies)
admin.site.register(action_movies)
admin.site.register(horror_movies)
admin.site.register(kids_movies)
admin.site.register(Video)
