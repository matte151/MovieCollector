from django.contrib import admin
# import your models here
from .models import Movie, Rental

# Register your models here
admin.site.register(Movie)
admin.site.register(Rental)