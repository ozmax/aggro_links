import json
import requests
import urllib

from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from rest_framework.authtoken.models import Token

from aggro_links.forms import UsernameForm


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



@require_http_methods(["GET", ])
def google_login(request):
    code = request.GET.get('code', None)
    exchange_url = "https://www.googleapis.com/oauth2/v4/token"
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    data = {
        'code': code,
        'client_id': settings.GOOGLE_CLIENT_ID,
        'client_secret': settings.GOOGLE_CLIENT_SECRET,
        'redirect_uri': 'http://ozmaxplanet.com:8000/auth/google/',
        'grant_type': 'authorization_code'
    }
    enc = urllib.urlencode(data)
    response = requests.post(exchange_url, data=enc, headers=headers)
    data = json.loads(response.content)
    token = data['access_token']
    headers = {'Authorization': 'Bearer '+token}
    info_url = "https://www.googleapis.com/oauth2/v3/userinfo"
    response = requests.get(info_url, headers=headers)
    user_data = json.loads(response.content)
    email = user_data['email']
    try:
        u = User.objects.get(email=email)
        token, _ = Token.objects.get_or_create(user=u)
        return redirect("http://ozmax.github.io/new/#/get_token?token={}".format(token))
        #return redirect("http://localhost/~ozmax/ozmax.github.io/new/#/get_token?token={}".format(token))
    except User.DoesNotExist:
        request.session['email'] = email
        return redirect(reverse('make_username'))
    return HttpResponse(response.content)


@require_http_methods(["GET", "POST" ])
def oauth2_username(request):
    form = UsernameForm(request.POST or None)
    print form
    email = request.session['email']
    print request.method
    if form.is_valid():
        print 'inside'
        inst = form.save(email)
        token, _ = Token.objects.get_or_create(user=inst)
        #redirect to client **for now
        return redirect("http://ozmax.github.io/new/#/get_token?token={}".format(token))
    tpl = 'aggro_links/username.html'
    context = {'form': form}
    return render(request, tpl, context)
