from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def index(request):
	if request.session['status']:
		leagues = Relationships.objects.filter(player=request.session['id']).order_by('name')
		context = {'leagues': leagues}
		#have html display league names
		#add game total
		#add ranking http://stackoverflow.com/questions/9647202/ordinal-numbers-replacement
		return render(request, 'ping_pong/index.html', context)
	return redirect('login:index')

def join_league(request):
	name = request.POST['league']
	password = request.POST['password']
	if Leagues.objects.authenticate_league(name, password):
		errors = Leagues.objects.player_in_League(name, request.session['id'])
		if len(errors) == 0:
			u = Leagues.objects.get(name=name)
			return redirect('league/'+u.id)
		else:
			messages.add_message(request, messages.ERROR, errors[0])
			return redirect('ping_pong:index')
	else:
		messages.add_message(request, messages.ERROR, 'invalid league login and password')
		return redirect('ping_pong:index')

def create_league(request):
	name = request.POST['create_name']
	password = request.POST['create_password']
	confirm = request.POST['create_confirm']
	errors = []
	errors += Leagues.objects.validate_league(name, password, confirm)
	if len(errors) == 0:
		errors = Leagues.objects.create_league(name, password)
		if len(errors) == 0:
			l = Leagues.objects.get(name=name)
			pid = request.session['id']
			Relationships.objects.create(player=pid, league=l.id)
			return redirect('league/'+ l)
	for e in errors:
		messages.add_message(request, messages.ERROR, e)
	return redirect('ping_pong:index')

def league(request, id):
	if request.session['status']:
		context = {}
		return render(request, 'ping_pong/league.html', context)
	return redirect('login:index')
