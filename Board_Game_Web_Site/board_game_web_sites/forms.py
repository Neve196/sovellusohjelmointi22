from django import forms

from . models import Board_game, Review

class GameForm(forms.ModelForm):
    class Meta:
        model = Board_game
        fields = ['name','description']
        labels = {'name':'Name:','description':'Description:'}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['my_review', 'stars']
        labels = {'my_review':'Date:'}
        widgets = {'my_review': forms.Textarea(attrs={'cols': 80})}
