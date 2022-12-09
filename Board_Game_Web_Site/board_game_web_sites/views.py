from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
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

def game(request, game_id):
    """Show a single game"""
    game = get_object_or_404(Board_game, id=game_id)
    context = {'game': game}
    return render(request, 'board_game_web_sites/board_game.html', context)