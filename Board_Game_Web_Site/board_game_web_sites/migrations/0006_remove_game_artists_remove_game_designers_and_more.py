# Generated by Django 4.1.3 on 2022-12-08 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_game_web_sites', '0005_rename_board_game_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='artists',
        ),
        migrations.RemoveField(
            model_name='game',
            name='designers',
        ),
        migrations.RemoveField(
            model_name='game',
            name='publishers',
        ),
        migrations.RemoveField(
            model_name='game',
            name='year_published',
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.CharField(max_length=10, null=True),
        ),
    ]