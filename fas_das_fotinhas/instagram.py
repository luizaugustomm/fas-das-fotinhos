
import requests

class Client():
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.access_token = None

    def get_auth_url(self):
        return 'https://api.instagram.com/oauth/authorize/?client_id={}&redirect_uri={}&response_type=code'.format(self.client_id, self.redirect_uri)

    def exchange_for_token(self, code):
        r = requests.post('https://api.instagram.com/oauth/access_token',
                          data={'client_id': self.client_id,
                                'client_secret': self.client_secret,
                                'grant_type': 'authorization_code',
                                'redirect_uri': self.redirect_uri,
                                'code': code})
        response = r.json()
        self.access_token = response.get('access_token')
        return self.access_token

    def revoke_access(self):
        if self.access_token:
            self.access_token = None

    def get_me(self):
        url = 'https://api.instagram.com/v1/users/self/?access_token={}'
        r = requests.get(url.format(self.access_token))
        response = r.json()
        return response.get('data')

    def get_user(self, user_id):
        url = 'https://api.instagram.com/v1/users/{}/?access_token={}'
        r = requests.get(url.format(user_id, self.access_token))
        response = r.json()
        return response.get('data')

    def get_recent_medias(self, count=15):
        url = 'https://api.instagram.com/v1/users/self/media/recent/?access_token={}&count={}'
        r = requests.get(url.format(self.access_token, count))
        response = r.json()
        return response.get('data')

    def get_media_likes(self, media_id):
        url = 'https://api.instagram.com/v1/media/{}/likes?access_token={}'
        r = requests.get(url.format(media_id, self.access_token))
        response = r.json()
        return response.get('data')
