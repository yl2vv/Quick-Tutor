from django.shortcuts import render
from .models import Tutee,Tutor, Profile

# Create your views here.
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from allauth.socialaccount import models as socialmodel



# Create your views here.


def login(request):
    return render(request, 'login/index.html')


def loggedin(request):
    # add code to store info from google into models
    #profile = googleUser.getBasicProfile()
    # if form not complete for user -> render form page
    # if(request.method == "POST"):
    #     name = request.POST['Name']
    #     email = request.POST['Email']
    #     image = request.POST['Image']
    #     ID = request.POST['ID']
    #     latitude = request.POST['Latitude']
    #     longitude = request.POST['Longitude']
    #     try:
    #         user = User.objects.get(userid=ID)
    #         formCheck = user[formCompleted]
    #         if(formCheck == False):
    #             return HttpResponseRedirect(reverse('login:form'))
    #     except:
    #         #User.objects.create(userid = ID,email = email,name = name,image = image,latitude = latitude, longitude = longitude)
    #         print("exception")
    s = socialmodel.SocialAccount.objects.get(user=request.user).extra_data
    email = s.get('email')
    uid = s.get('id')
    name = s.get('name')
    picture = s.get('picture')
    currentProfile = Profile.objects.get(user=request.user)
    currentProfile.email = email
    currentProfile.image = picture
    #currentProfile.Uid = uid
    currentProfile.save()
    if request.user.is_authenticated:
      return HttpResponseRedirect(reverse('login:home'))
    else:
        return HttpResponseRedirect(reverse('login:login'))


def form(request):
    return render(request, 'login/form.html')


def home(request):
    return render(request, 'login/home.html')

# view for the tutor page after user has clicked that option on the homepage
def tutoring(request):
    return render(request, 'tutor/main.html')

# view for the tutor page after user has clicked that option on the homepage
def tuteeing(request):
    return render(request, 'tutee/main.html')