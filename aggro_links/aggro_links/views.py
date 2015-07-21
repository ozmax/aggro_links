import requests
import urllib
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse


@require_http_methods(["GET", ])
def activation_frontend(request, uid=None, token=None):
    if uid and token:
        payload = {
            'uid': uid,
            'token': token
            }
        enc = urllib.urlencode(payload)
        url = 'http://localhost:8000/auth/activate/'
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(url, data=enc, headers=headers)
        if response.status_code == 200:
            return HttpResponse("ACTIVATED")
        else:
            return HttpResponse(response.text)
