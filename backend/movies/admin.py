from django.contrib import admin
from .models import Movie, Rating, Favorite, Tag

admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(Tag)
