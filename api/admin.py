from django.contrib import admin
from .models import Movie, Rating, Actor, Producer

# Register your models here.

admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Actor)
admin.site.register(Producer)
