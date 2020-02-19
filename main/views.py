from django.shortcuts import render
from .models import Tutee,Tutor,Profile

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
    #add code to store info from google into models
    #profile = googleUser.getBasicProfile()
    return HttpResponseRedirect(reverse('login:home'))

def home(request):
    return render(request, 'login/home.html')

def newprofile(request):
    context = {
        'profiles' : Profile.objects.all()
    }
    return render(request, 'login/newprofile.html', context)