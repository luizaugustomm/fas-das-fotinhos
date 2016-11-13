
import requests

class Client():
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def get_auth_url(self):
        return 'https://api.instagram.com/oauth/authorize/?client_id={}&redirect_uri={}&response_type=code'.format(self.client_id, self.redirect_uri)

    def exchange_for_token(self, code):
        r = requests.post('https://api.instagram.com/oauth/access_token',
                          params={'client_id': self.client_id,
                                  'client_secret': self.client_secret,
                                  'grant_type': 'authorization_code',
                                  'redirect_uri': self.redirect_uri,
                                  'code': code})
        response = r.json()
        return response.get('access_token')
