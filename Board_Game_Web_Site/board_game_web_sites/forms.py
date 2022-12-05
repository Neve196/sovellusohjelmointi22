from django import forms

from .models import Board_game

class Board_gameForm(forms.ModelForm):
    class Meta:
        model = Board_game
        fields = ["name", "description", "number_of_players"]
        labels = {"name":"", "description": "", "number_of_players": ""}