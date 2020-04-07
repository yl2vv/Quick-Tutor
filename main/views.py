from django.shortcuts import render
from .models import Tutee,Tutor,Profile, Question
import re

# Create your views here.
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from allauth.socialaccount import models as socialmodel
import math


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
    if(request.method == 'POST'):
        p = Profile.objects.get(user=request.user)
        p.latitude = request.POST.get('Latitude')
        p.longitude = request.POST.get('Longitude')
        p.save()
        if(request.POST.get('Type') == 'tutee'):
            return HttpResponseRedirect(reverse('login:tutee'))
        if(request.POST.get('Type') == 'tutor'):
            return HttpResponseRedirect(reverse('login:tutor'))
    return render(request, 'login/home.html')

# view for the tutor page after user has clicked that option on the homepage
def tutoring(request):
    o = Profile.objects.get(user=request.user)
    connection = o.connection
    if connection != "":
        tutee = Profile.objects.get(pk=connection)
        question = Question.objects.get(person=tutee)
        context = {
            "first": tutee.firstname,
            "last": tutee.lastname,
            "question": question,
        }
    else:
        context = {
                "first": "No",
                "last": "one",
                "question": "a question.",
            }
    return render(request, 'tutor/main.html', context)

# view for the tutee page after user has clicked that option on the homepage
def tuteeing(request):
    #Get current user
    o = Profile.objects.get(user=request.user)
    classes = o.classes
    #After clicking submit
    if request.method == "POST":
        #Get the user inputs
        question = request.POST.get('Question')
        class_id = request.POST.get('class')
        file_upload = request.POST.get('upload')
        comments = request.POST.get('comments')
        #Store in model
        obj = Question() 
        obj.Question_text = question
        obj.Class_text = class_id
        obj.File_upload = file_upload
        obj.Comments_text = comments
        obj.asker = o.id
        obj.person = Profile.objects.get(user=request.user)
        obj.save()
        o.save()
        return HttpResponseRedirect('tuteeing/results')
    context = {
         "classes": classes,
    }
    return render(request, 'tutee/main.html', context)

def results(request):
    #Grab all the questions
    questions = Question.objects.all()
    #Grab all the profiles
    people = Profile.objects.all()
    me = Profile.objects.get(user=request.user)
    results = []
    #Check that a person took the class and is currently an active tutor 
#WILL HAVE TO ADD LOCATION AS WELL
    for p in people:
        if questions.last().Class_text.upper() in p.classes:
            if p.activeStatus == True:
                if(math.sqrt((me.latitude - p.latitude)**2 + (me.longitude - p.longitude)**2) < 0.015):
                    results.append(p)
    context = {
        "questions_list": questions,
        "people_list": people,
        "results": results,
    }
    return render(request, 'tutee/results.html', context)

def rating(request, tutor_id):
    #Get the tutor by the tutor_id set in results page
    tutor = Profile.objects.get(pk=tutor_id)
    tutor.connection = Profile.objects.get(user=request.user).id
    tutor.save()
    if request.method == "POST":
        #Increment total rating 
        tutor.compositeRating = tutor.compositeRating + int(request.POST.get("rate"))
        #Increment times tutored
        tutor.timesTutored = tutor.timesTutored + 1
        #Calcuate the rating of the tutor
        tutor.tutorRate = tutor.compositeRating / tutor.timesTutored
        #Break connections and delete question
        tutor.connection = ""
        tutor.save()
        me = Profile.objects.get(user=request.user)
        question = Question.objects.get(person = me)
        question.delete()
        me.save()

        #Return Home
        return HttpResponseRedirect('/home')
    context = {
        'tutor' : tutor
    }
    return render(request, "tutee/ratings.html", context)

def newprofile(request):
    if request.method == "POST":
        o = Profile.objects.get(user=request.user)
        o.firstname = request.POST.get('FirstName')
        o.lastname = request.POST.get('LastName')
        o.save()
        return HttpResponseRedirect('newprofile1')
    return render(request, 'login/newprofile.html')

def newprofile1(request):
    if request.method == "POST":
        o = Profile.objects.get(user=request.user)
        o.phoneNumber = request.POST.get('PhoneNumber')
        o.computingID = request.POST.get('ComputingID')
        o.save()
        return HttpResponseRedirect('newprofile2')
    return render(request, 'login/newprofile1.html')

def newprofile2(request):
    # this deals with classes
    o = Profile.objects.get(user=request.user)
    if request.method == "POST" and len(o.classes) == 0:
        full_string = str(request.POST.get('Classes'))
        split_list = full_string.split(",")
        for i in split_list:
            if re.match(r"[A-Z]{2,4}[0-9]{4}$",i):
                o.classes.append(i)
                o.save()
        return HttpResponseRedirect('newprofile2.5')
    elif request.method == "POST" and len(o.classes) != 0:
        return HttpResponseRedirect('newprofile3')
    return render(request, 'login/newprofile2.html')

def newprofile2_5(request):
    o = Profile.objects.get(user = request.user)
    classes = o.classes
    context = {
        "classes": classes,
    }
    if request.method == "POST":
        return HttpResponseRedirect('newprofile3')
    return render(request, 'login/newprofile2.5.html', context)

def newprofile3(request):
    if request.method == "POST":
        o = Profile.objects.get(user = request.user)
        o.bio = request.POST.get('Bio')
        o.gpa = request.POST.get('GPA')
        o.schoolYear = request.POST.get('SchoolYear')
        o.formCompleted = True
        o.save()
        return HttpResponseRedirect(reverse('login:home'))
    return render(request,'login/newprofile3.html')



def userprofile(request):
    o = Profile.objects.get(user = request.user)
    context = {
         "user": o,
    }
    return render(request, 'login/userprofile.html', context)

def question(request):
    return render(request, 'tutee/question.html')

def session(request):
    return render(request, 'tutor/session.html')