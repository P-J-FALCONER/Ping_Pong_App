from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def index(request):
    return render(request, 'login/index.html')

def register(request):
    reg_username = request.POST['username']
    reg_first_name = request.POST['first_name']
    reg_last_name = request.POST['last_name']
    reg_email = request.POST['email']
    reg_birthday = request.POST['birthday']
    reg_password = request.POST['password']
    reg_confirm = request.POST['confirm']
    errors = []
    errors += Players.objects.validate_user(reg_username, reg_first_name, reg_last_name, reg_email, reg_birthday, reg_password, reg_confirm)
    if len(errors) == 0:
        errors = Players.objects.create_user(reg_username, reg_first_name, reg_last_name, reg_email, reg_birthday, reg_password)
        if len(errors) == 0:
            request.session['status']=True
            request.session['id']=errors.id
            request.session['name']=errors.first_name
            return redirect('ping_pong:index')
    for e in errors:
        messages.add_message(request, messages.ERROR, e)
    return redirect('login:index')

def authenticate(request):
    login_username = request.POST['username_login']
    login_password = request.POST['password_login']
    if Players.objects.authenticate_user(login_username, login_password):
        u = Players.objects.get(username=login_username)
        request.session['id']=u.id
        request.session['name']=u.first_name
        request.session['status']=True
        return redirect('ping_pong:index')
    else:
        messages.add_message(request, messages.ERROR, 'invalid login')
        return redirect('login:index')

def logout(request):
    request.session.flush()
    return redirect('login:index')