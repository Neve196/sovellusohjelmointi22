from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from board_game_web_sites.models import User


# Create your models here.
class UserBorrows(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name = 'user_borrows')
    nro = models.IntegerField(default = 0)

    @receiver(post_save, sender = User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created: 
            UserBorrows.objects.create(user = instance)

    @receiver(post_save, sender = User)
    def save_user_profile(sender, instance, **kwargs):
        instance.user_borrows.save()