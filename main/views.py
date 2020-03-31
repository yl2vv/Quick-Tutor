from django.shortcuts import render
from .models import Tutee,Tutor,Profile

# Create your views here.
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
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
    if(Profile.objects.filter(user=request.user).exists() == False):
        s = socialmodel.SocialAccount.objects.get(user=request.user).extra_data
        email = s.get('email')
        uid = s.get('id')
        name = s.get('name')
        picture = s.get('picture')
        currentProfile = Profile(user=request.user,email=email,image=picture,Uid=uid)
        currentProfile.save()
    if request.user.is_authenticated:
        if Profile.objects.get(user=request.user).formCompleted == False:
            return HttpResponseRedirect(reverse('login:newprofile'))
        return HttpResponseRedirect(reverse('login:home'))
    else:
        return HttpResponseRedirect(reverse('login:login'))

def home(request):
    return render(request, 'login/home.html')

# view for the tutor page after user has clicked that option on the homepage
def tutoring(request):
    return render(request, 'tutor/main.html')

# view for the tutor page after user has clicked that option on the homepage
def tuteeing(request):
    return render(request, 'tutee/main.html')

def newprofile(request): #maybe try to change to (request,id) if way to handle positional argument
    if request.method == "POST":
        # o = User.objects.get(userid=id)
        o = Profile.objects.get(user=request.user)
        o.firstName = request.POST.get('FirstName')
        o.lastName = request.POST.get('LastName')
        # o.computingID = request.POST.get('ComputingID')
        o.phoneNumber = request.POST.get('PhoneNumber')
        o.gpa = request.POST.get('GPA')
        # o.schoolYear = request.POST.get('SchoolYear')
        # o.bio = request.POST.get('Bio')
        o.formCompleted = True

         #get current user to add this info to User.objects.get(userid=ID)
        # o.firstName = newfirstname
        # o.lastName = newlastname
        # o.computingID = newcomputingid
        # o.phoneNumber = newphonenumber
        # o.gpa = newgpa
        # o.schoolYear = newschoolyear
        # o.bio = newbio
        o.save()
        return HttpResponseRedirect(reverse('login:home'))

    return render(request, 'login/newprofile.html')

def userprofile(request):
    return render(request, 'login/userprofile.html')

def question(request):
    return render(request, 'tutee/question.html')

def session(request):
    return render(request, 'tutor/session.html')