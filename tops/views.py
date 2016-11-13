from django.shortcuts import render, redirect
from fas_das_fotinhas.settings import DEBUG, CLIENT_ID, CLIENT_SECRET

import requests


if DEBUG:
    redirect_uri = '127.0.0.1:8080/auth_done'
else:
    redirect_uri = 'fas-das-fotinhas.herokuapp.com/auth_done'


def auth(request):
    url = 'https://api.instagram.com/oauth/authorize/?client_id={}&redirect_uri={}&response_type=code'.format(CLIENT_ID, redirect_uri)
    return render(request, 'auth.html', {'auth_url' : url})

def index(request):
    if 'access_token' not in request.session:
        return redirect('auth')
    return render(request, 'index.html')
