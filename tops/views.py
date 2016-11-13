from django.shortcuts import render, redirect
from fas_das_fotinhas.settings import DEBUG, CLIENT_ID, CLIENT_SECRET
from fas_das_fotinhas.client import Client

import requests

DEBUG = False
if DEBUG:
    redirect_uri = '127.0.0.1:8080/auth_done'
else:
    redirect_uri = 'http://fas-das-fotinhas.herokuapp.com/auth_done'


client = Client(CLIENT_ID, CLIENT_SECRET, redirect_uri)


def auth(request):
    auth_url = client.get_auth_url()
    return render(request, 'auth.html', {'auth_url' : auth_url})

def auth_done(request):
    code = request.GET.get('code')
    access_token = client.exchange_for_token(code)
    request.session['access_token'] = access_token
    return redirect('index')

def index(request):
    if 'access_token' not in request.session:
        return redirect('auth')
    return render(request, 'index.html')
