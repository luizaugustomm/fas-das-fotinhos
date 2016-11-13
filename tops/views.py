from collections import OrderedDict

from django.shortcuts import render, redirect
from fas_das_fotinhas.settings import DEBUG, CLIENT_ID, CLIENT_SECRET
from fas_das_fotinhas.instagram import Client

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

def logout(request):
    request.session.pop('access_token')
    client.revoke_access()
    return redirect('auth')

def index(request):
    if 'access_token' not in request.session:
        return redirect('auth')
    me = client.get_me()
    medias = client.get_recent_medias()
    fans = {}
    for media in medias:
        likes = client.get_media_likes(media.get('id'))
        for like in likes:
            if like.get('username') not in fans:
                fans['username'] = {
                    'id': like.get('id'),
                    'first_name': like.get('first_name'),
                    'last_name': like.get('last_name'),
                    'likes': 1
                }
            else:
                fans['username']['likes'] += 1
    sorted_fans = OrderedDict(sorted(fans.items(),
                                  key=lambda kv: kv[1]['likes'], reverse=True))
    return render(request, 'index.html', {'me': me, 'fans' : sorted_fans})
