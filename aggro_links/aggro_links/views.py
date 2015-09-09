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

from aggro_links.oauth2 import Oauth2
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
def oauth2_login(request):
    code = request.GET.get('code', None)
    state = request.GET.get('state', None)
    g_oauth2 = Oauth2(code, state)
    g_oauth2.do_oauth2()
    email = g_oauth2.get_email()
    try:
        u = User.objects.get(email=email)
        token, _ = Token.objects.get_or_create(user=u)
        return redirect("http://ozmax.github.io/new/#/get_token?token={}".format(token))
    except User.DoesNotExist:
        request.session['email'] = email
        return redirect(reverse('make_username'))
    return HttpResponse(response.content)


@require_http_methods(["GET", "POST" ])
def oauth2_username(request):
    form = UsernameForm(request.POST or None)
    email = request.session['email']
    if form.is_valid():
        inst = form.save(email)
        token, _ = Token.objects.get_or_create(user=inst)
        #redirect to client **for now
        return redirect("http://ozmax.github.io/new/#/get_token?token={}".format(token))
    tpl = 'aggro_links/username.html'
    context = {'form': form}
    return render(request, tpl, context)
