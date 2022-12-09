"""URL patterns"""

from django.urls import path

from . import views

app_name = 'board_game_web_sites'
urlpatterns = [
    # Home page
    path('',views.index, name='index'),
    # Page that shows all board games
    path('games/', views.games, name='games'),
    # Page for a single game
    path('games/<int:game_id>/',views.game, name='game'),
    # Page for adding a new game
    path('new_game/', views.new_game, name='new_game'),
]