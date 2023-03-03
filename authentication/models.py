from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'creator'),
        (SUBSCRIBER, 'subscriber')
    )

    profile_photo = models.ImageField()
    role =  models.CharField(max_length=30, choices=ROLE_CHOICES)

