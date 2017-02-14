from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^index$', index, name='index'),
	url(r'^join_league$', join_league, name='join_league'),
	url(r'^create_league$', create_league, name='create_league'),
	url(r'^league/(?P<id>\d+$)',  league, name='league'),
]
