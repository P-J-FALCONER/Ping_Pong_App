from __future__ import unicode_literals
from ..ping_pong.models import *
import bcrypt
import re
from django.db import models
from django.db import IntegrityError
from datetime import *

REGEX_EMAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
REGEX_PASSWORD  = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

class PlayersManager(models.Manager):
	def validate_user(self, username, first_name, last_name, email, birthday, password, confirm):
		errors = []
		if len(username) < 3:
			errors.append('Username needs to get greater than 2 characters')
		if len(first_name) < 3:
			errors.append('First name needs to get greater than 2 characters')
		if len(last_name) < 3:
			errors.append('Last name needs to get greater than 2 characters') 
		if REGEX_EMAIL.search(email) is None:
			errors.append('Invalid email')
		if datetime.strptime(birthday, '%Y-%m-%d') > datetime.now():
			errors.append('Birthday cannot be in the future')
		if REGEX_PASSWORD.search(password) is None:
			errors.append('password too weak')
		if password != confirm:
			errors.append('passwords do not match')
		return errors

	def create_user(self, username, first_name, last_name, email, birthday, password):
		errors = []
		try:
			hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			Players.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, birthday=birthday, password=hashed)
		except:
			errors.append('Username already exists')
		return errors

	def authenticate_user(self, username, password):
		try:
			user = Players.objects.get(username=username)
			return bcrypt.hashpw(password.encode(), user.password.encode()) == user.password
		except:
			return False


class Players(models.Model):
	username = models.CharField(max_length=50, unique=True)
	first_name = models.CharField(max_length=35)
	last_name = models.CharField(max_length=35)
	email = models.CharField(max_length=255)
	birthday = models.DateField()
	password = models.CharField(max_length=255)
	league = models.ManyToManyField('ping_pong.Leagues')
	objects = PlayersManager()
