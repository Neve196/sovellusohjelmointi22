from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from . models import Board_game
from . forms import GameForm

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

def new_game(request):
    '''Add a new game'''
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = GameForm()
    else:
        # POST data submitted; process data.
        form = GameForm(request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.save()
            return HttpResponseRedirect(reverse('board_game_web_sites:games'))

    context = {'form': form}
    return render(request, 'board_game_web_sites/new_game.html', context)