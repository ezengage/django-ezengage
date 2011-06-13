#coding=utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden,HttpResponse,HttpResponseNotFound,HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from django.contrib import auth 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def token_login(request):
    token = request.POST.get('token', None)
    user = auth.authenticate(eze_token = token)
    next = request.GET.get('next', '/')
    if user:
        auth.login(request, user)
        return HttpResponseRedirect(next)
    else:
        return HttpResponse('Fail to login via ezengage')

