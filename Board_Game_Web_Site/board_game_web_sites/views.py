from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for Board Game Web Site."""
    return render(request, 'board_game_web_sites/index.html')