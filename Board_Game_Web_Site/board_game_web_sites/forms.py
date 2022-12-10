from django import forms

from . models import Board_game

class GameForm(forms.ModelForm):
    class Meta:
        model = Board_game
        fields = ['name']
        labels = {'name':''}

