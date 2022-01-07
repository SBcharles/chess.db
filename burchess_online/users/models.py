import uuid

from django.db import models

# Create your models here.


class User(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    username = models.CharField(
        max_length=50,
        unique=True,
        help_text='Required. <51 characters. @/./+/-/_ only',
        error_messages={
            'unique': "Sorry, that username is taken!"
        }
    )
    email = models.EmailField(
        name='email_address',  # is 'name' right kwarg?
        max_length=254,
        unique=True,
    )

    # elo_rating = models.IntegerField()
    # ranking = models.IntegerField()

    def __str__(self):
        return self.email
