from django.contrib import admin
from .models import CustomUser, movie, Profile, video

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(movie)
admin.site.register(Profile)
admin.site.register(video)
