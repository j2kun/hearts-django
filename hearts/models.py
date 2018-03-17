from django.db import models
from django.utils import timezone


class Game(models.Model):
    created = models.DateTimeField(default=timezone.now)
