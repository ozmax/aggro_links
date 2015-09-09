import requests
import json
import urllib
from django.conf import settings


class Oauth2(object):
    
    def __init__(self, code, type):
        self.code = code
        self.type = type
        self.headers = {'content-type': 'application/x-www-form-urlencoded'}
        self.client_id = getattr(settings, '{}_CLIENT_ID'.format(type))
        self.client_secret = getattr(settings, '{}_CLIENT_SECRET'.format(type))
        self.redirect_uri = getattr(settings, '{}_REDIRECT_URI'.format(type))
        self.info_url = getattr(settings, '{}_INFO_URL'.format(type))

    def exchange_code(self):
        exchange_url = getattr(settings,'{}_EXCHANGE_URL'.format(self.type))
        exchange_data = {
            'code': self.code,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'authorization_code'
        }
        encoded_data = urllib.urlencode(exchange_data)
        response = requests.post(exchange_url, data=encoded_data, headers=self.headers)
        print response.content
        data = json.loads(response.content)
        self.token = data['access_token']

    def get_user_info(self):
        if self.type == 'FB':
            parameters = "?fields=email"
        else:
            parameters = ''
        headers = {'Authorization': 'Bearer {}'.format(self.token)}
        response = requests.get(self.info_url+parameters, headers=headers)
        user_data = json.loads(response.content)
        email = user_data['email']
        self.email = email

    def get_email(self):
        return self.email

    def do_oauth2(self):
        self.exchange_code()
        self.get_user_info()
