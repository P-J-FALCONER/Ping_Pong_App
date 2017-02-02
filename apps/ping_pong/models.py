from __future__ import unicode_literals
from ..login.models import *
from django.db import models
import bcrypt

class Leagues(models.Model):
	name = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Games(models.Model):
	winner = models.ForeignKey(Players, related_name='winner_to_player')
	winner_score = models.PositiveSmallIntegerField()
	winner_new_rating = models.PositiveSmallIntegerField()
	loser = models.ForeignKey(Players, related_name='loser_to_player')
	loser_score = models.PositiveSmallIntegerField()
	loser_new_rating = models.PositiveSmallIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

