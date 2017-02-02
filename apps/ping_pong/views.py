from django.shortcuts import render, HttpResponse
from models import *

# Create your views here.
def index(request):
	return render(request, 'ping_pong/index.html')
def join_league(request):
	name = request.POST['league']
	password = request.POST['password']
	#authentic league make sure league is existing and that player is not in league
	#if no league flash no league and redirect to index page
	#if league but user not in in add them to league using session.id
	#if league and user are already in league the direct to league page
	#direct to league page if added to league.
	pass
def create_league(request):
	#look if league is already existing
	#if it is redirect to index and flash
	#if password do not match redirect and flash
	#if created successful redirect to league page
	pass		