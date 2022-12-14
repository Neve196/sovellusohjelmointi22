from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from . models import Board_game, Review
from . forms import GameForm, ReviewForm

# Create your views here.

def index(request):
    """The home page for Board Game Web Site"""
    return render(request, 'board_game_web_sites/index.html')

@login_required
def games(request):
    """Show all board games"""
    games = Board_game.objects.order_by('date_added')
    context = {'games':games}
    return render(request, 'board_game_web_sites/board_games.html', context)

@login_required
def game(request, game_id):
    """Show a single game and all its reviews"""
    game = get_object_or_404(Board_game, id=game_id)
    reviews = game.review_set.order_by('-date_added')
    context = {'game': game, 'reviews':reviews}
    return render(request, 'board_game_web_sites/board_game.html', context)

@login_required
def new_game(request):
    '''Add a new game'''
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = GameForm()
    else:
        # POST data submitted; process data.
        form = GameForm(data=request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.owner = request.user
            new_game.save()
            return HttpResponseRedirect(reverse('board_game_web_sites:games'))

    context = {'form': form}
    return render(request, 'board_game_web_sites/new_game.html', context)

@login_required
def reviews(request, game_id):
    game = Board_game.objects.get(id = game_id)
    reviews = Review.objects.order_by('date_added')
    context = {'reviews': reviews}
    return render(request, 'board_game_web_sites/reviews.html', context)
    
@login_required
def new_review(request, game_id):
    """Add a new review for a particular game."""
    game = Board_game.objects.get(id=game_id)
 
    if request.method != 'POST':
 # No data submitted; create a blank form.
        form = ReviewForm()
    else:
 # POST data submitted; process data.
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.game = game
            new_review.owner = request.user
            new_review.save()
            return redirect('board_game_web_sites:game', game_id= game_id)
 # Display a blank or invalid form.
    context = {'game': game, 'form': form}
    return render(request, 'board_game_web_sites/new_review.html', context)

@login_required
def edit_review(request, review_id):
    """Edit an existing review."""
    review = Review.objects.get(id=review_id)
    game = review.game
    if review.owner != request.user:
        raise Http404
 
    if request.method != 'POST':
    # Initial request; pre-fill form with the current review.
        form = ReviewForm(instance=review)
    else:
 # POST data submitted; process data.
        form = ReviewForm(instance=review, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('board_game_web_sites:game', game_id=game.id)
    context = {'review': review, 'game': game, 'form': form}
    return render(request, 'board_game_web_sites/edit_review.html', context)