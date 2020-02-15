from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader

# Create your views here.
def login(request):
    return render(request, 'login/index.html')

def loggedin(request):
    #client id
    #173138853341-9hdlujjsgpq28e3iite0n29tc1artuhr.apps.googleusercontent.com

    #client secret
    #BTJ22vrZSuwsT1FYEvWZ34Fs
    return