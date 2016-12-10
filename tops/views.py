
from django.shortcuts import render, redirect
from fas_das_fotinhos.settings import DEBUG, CLIENT_ID, CLIENT_SECRET
from fas_das_fotinhos.instagram import Client

import requests

if DEBUG:
    redirect_uri = '127.0.0.1:8080/auth_done'
else:
    redirect_uri = 'http://fas-das-fotinhos.herokuapp.com/auth_done'


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
    client.allow_access(request.session.get('access_token'))
    me = client.get_me()
    medias = client.get_recent_medias()
    fans = {}
    for media in medias:
        likes = client.get_media_likes(media.get('id'))
        for like in likes:
            username = like.get('username')
            if username not in fans:
                fans[username] = {
                    'id': like.get('id'),
                    'full_name' : like.get('full_name'),
                    'profile_picture' : like.get('profile_picture'),
                    'likes': 1
                }
            else:
                fans[username]['likes'] += 1
    fans = sorted(fans.items(), key=lambda x: x[1]['likes'], reverse=True)[:100]
    for username, data in fans:
        data['like_percent'] = data.get('likes') / 50.0 * 100
    return render(request, 'index.html', {'me': me, 'fans' : fans})

def privacy(request):
    return render(request, 'privacy-policy.html')
