from django import forms

from . models import Board_game, Review

class GameForm(forms.ModelForm):
    class Meta:
        model = Board_game
        fields = ['name']
        labels = {'name':''}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text',]
        labels = {'text':'Review:'}
        widgets = {'text':forms.Textarea(attrs={'cols': 80})}