from django.db import models

# Models
class Board_game(models.Model) :
    # Name of board game
    name = models.CharField(max_length=200)
    players = models.CharField(max_length=10, null=True)
    # Automatically applies date when board game is added
    date_added = models.DateTimeField(auto_now_add=True)
    # Automatically applies date when board game is modified
    date_modified = models.DateTimeField(auto_now=True)
    # Returns a string representation of the model
    def __str__(self):
        return self.name
    
class Review(models.Model):
    # Review of a board game
    my_review = models.TextField(max_length=250)
    # Star rating of a board game
    stars = models.IntegerField()
    # Automatically applies date when a review is added
    date_added = models.DateTimeField(auto_now_add=True)
    # Automatically applies date when review is modified
    date_modified = models.DateTimeField(auto_now=True)
    # Allows a review to be connected to a board game
    board_game = models.ForeignKey(Board_game, on_delete=models.CASCADE)
    # Returns a 50 character string representation of the model
    def __str__(self):
        return f"{self.my_review[:50]}..."
