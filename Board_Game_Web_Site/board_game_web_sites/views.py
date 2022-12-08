from django.shortcuts import render
from . models import Board_game

# Create your views here.

def index(request):
    """The home page for Board Game Web Site"""
    return render(request, 'board_game_web_sites/index.html')

def games(request):
    """Show all board games"""
    games = Board_game.objects.order_by('date_added')
    context = {'games':games}
    return render(request, 'board_game_web_sites/board_games.html', context)