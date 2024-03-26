from django.contrib import admin
from .models import Movie

# Register your models here.

admin.site.add_action(Movie)