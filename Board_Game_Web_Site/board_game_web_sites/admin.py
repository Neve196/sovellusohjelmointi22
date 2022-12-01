from django.contrib import admin

# Register your models here.

from .models import Board_game, Review

admin.site.register(Board_game)
admin.site.register(Review)
