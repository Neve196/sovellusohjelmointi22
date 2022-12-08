"""URL patterns"""

from django.urls import path

from . import views

app_name = 'board_game_web_sites'
urlpatterns = [
    # Home page
    path('',views.index, name='index'),
]