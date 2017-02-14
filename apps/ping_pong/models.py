from __future__ import unicode_literals
from ..login.models import *
from django.db import models
import bcrypt
import re

REGEX_EMAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
REGEX_PASSWORD  = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z]{8,}$')

class LeagueManager(models.Manager):
	def validate_league(self, name, password, confirm):
		errors = []
		if len(name) < 3:
			errors.append('League name needs to get greater than 2 characters')
		if False: #REGEX_PASSWORD.search(password) is None:
			errors.append('Password too weak')
		if password != confirm:
			errors.append('Passwords do not match')
		return errors
	def player_in_League(self, name, id):
		errors = []
		try:
			Leagues.objects.get(players__id=id)
			errors = ['Player already in league']
			return errors
		except:
			return errors

	def create_league(self, name, password):
		errors = []
		lname = name
		try:
			hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			Leagues.objects.create(name=lname, password=hashed)
			return errors
		except:
			errors.append('League name already exists')
			return errors

	def authenticate_league(self, name, password):
		try:
			league = Leagues.objects.get(name=name)
			return bcrypt.hashpw(password.encode(), user.password.encode()) == league.password
		except:
			return False

class Leagues(models.Model):
	name = models.CharField(max_length=255, unique=True)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = LeagueManager()

class Relationships(models.Model):
	league = models.ForeignKey(Leagues, related_name='league')
	player = models.ForeignKey(Players, related_name='player')
	created_at = models.DateTimeField(auto_now_add=True)

class GameManager(models.Manager):
	def add(self):
		pass
	def delete(self):
		pass
	def update(self):
			pass	
class Games(models.Model):
	winner = models.ForeignKey(Players, related_name='winner_to_player')
	winner_score = models.PositiveSmallIntegerField()
	winner_new_rating = models.PositiveSmallIntegerField()
	loser = models.ForeignKey(Players, related_name='loser_to_player')
	loser_score = models.PositiveSmallIntegerField()
	loser_new_rating = models.PositiveSmallIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = GameManager()

class RatingManager(models.Manager):
	def add(self):
		pass
	def delete(self):
		pass
	def update(self):
		pass			

class Ratings(models.Model):
	player = models.ForeignKey(Players)
	rating = models.PositiveSmallIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = RatingManager()

