import uuid

from django.db import models

# Create your models here.
from users.models import User


class PlayerColour(models.TextChoices):
    WHITE = 'white', 'white'
    BLACK = 'black', 'black'


class Game(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    player_one = models.ForeignKey(
        to=User,
        colour=models.CharField(choices=PlayerColour.choices),
        on_delete=models.PROTECT,
        won=models.BooleanField(default=False)
    )
    player_two = models.ForeignKey(
        to=User,
        colour=models.CharField(choices=PlayerColour.choices),  # constrain this to be not p1.colour
        on_delete=models.PROTECT,
        won=models.BooleanField(default=False)
    )
