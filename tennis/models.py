# Create your models here.
from django.db import models


class Wins(models.Model):
    name = models.CharField(max_length=100)
    # wins = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Players(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    wins = models.ForeignKey(Wins, on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
