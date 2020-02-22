from django.shortcuts import render
from .models import Profile

from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader

#this view shows an already created profile (image, number of people tutored, etc. )
def userprofile(request):
    return render(request, 'profile_form/userprofile.html')  # figure out how to pull data from newprofile