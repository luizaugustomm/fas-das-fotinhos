from django.shortcuts import render, redirect
from fas_das_fotinhas.settings import DEBUG, CLIENT_ID, CLIENT_SECRET

import requests

DEBUG = False
if DEBUG:
    redirect_uri = '127.0.0.1:8080/auth_done'
else:
    redirect_uri = 'fas-das-fotinhas.herokuapp.com/auth_done'


def auth(request):
    url = 'https://api.instagram.com/oauth/authorize/?client_id={}&redirect_uri={}&response_type=code'.format(CLIENT_ID, redirect_uri)
    return render(request, 'auth.html', {'auth_url' : url})

def auth_done(request):
    code = request.GET.get('code')
    r = requests.post('https://api.instagram.com/oauth/access_token',
                      params={'client_id': CLIENT_ID,
                              'client_secret': CLIENT_SECRET,
                              'grant_type': 'authorization_code',
                              'redirect_uri': redirect_uri,
                              'code': code})
    response = r.json()
    access_token = response.get('access_token')
    request.session['access_token'] = access_token
    return redirect('index')

def index(request):
    if 'access_token' not in request.session:
        return redirect('auth')
    return render(request, 'index.html', {'at': request.session.get('access_token')})
