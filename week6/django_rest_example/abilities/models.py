from django.db import models

# Create your models here.
class Ability(models.Model):
    name = models.CharField(max_length=255)
    damage = models.IntegerField()
    icon = models.CharField(max_length=255)
    rarity = models.CharField(max_length=20)
