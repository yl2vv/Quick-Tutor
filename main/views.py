from django.shortcuts import render
from .models import Tutee,Profile, Question
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
    if(request.user != 'AnonymousUser'):
        try:
            p = Profile.objects.get(user=request.user)
            p.activeStatus = False
            p.save()
            # request.user.is_active = False
            # request.user.save()
            print('worked')
            return HttpResponseRedirect('accounts/logout')
        except:
            print('Anonymous User')
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
        #p.latitude = request.POST.get('Latitude')
        #p.longitude = request.POST.get('Longitude')
        # if(request.POST.get('Type') == 'tutee'):
        print(request.POST)
        if 'tutee' in request.POST:
            p.activeStatus = False
            p.save()
            return HttpResponseRedirect(reverse('login:tutee'))
        elif 'tutor' in request.POST:
            p.activeStatus = True
            p.save()
            return HttpResponseRedirect('tutoring')
    return render(request, 'login/home.html')

# view for the tutor page after user has clicked that option on the homepage
def tutoring(request):
    # if(request.method == 'POST'):
    #     p = Profile.objects.get(user=request.user)
    #     if(request.POST.get('leftPage') == True):
    #         p.activeStatus = False
    #         p.save()
    o = Profile.objects.get(user=request.user)
    connection = o.connection
    qr = o.questionsReceived
    questionsBool = False
    if connection != "":
        questionsBool = True
        try:
            tutee = Profile.objects.get(pk=connection)
            question = Question.objects.get(person=tutee)
            context = {
                "questionsReceived": questionsBool,
                "user": o,
                "tutee": tutee,
                "question": question
                }
        except:
            print("no question")
            context = {
            "questionsReceived": questionsBool,
            "user": o
        }
    elif len(qr) > 0:
        questionsBool = True
        tutees = []
        questions = []
        for q in qr:
            tutee = Profile.objects.get(pk=q)
            question = Question.objects.get(person=tutee)
            tutees.append(tutee)
            questions.append(question) 
        context = {
            "questionsReceived": questionsBool,
            "user": o,
            "tutees": tutees,
            "questions": questions,
                }
    else:
        context = {
            "questionsReceived": questionsBool,
            "user": o
        }
    return render(request, 'tutor/main.html', context)
    # return render(request, 'tutor/main.html')

# view for the tutor page after user has clicked that option on the homepage
def tuteeing(request):
    #Get current user
    o = Profile.objects.get(user=request.user)
    classes = o.classes
    #add person to tutee model if it's their first time asking a question
    if Tutee.objects.filter(person = o).count() == 0:
        tutee = Tutee(person=o)
        tutee.save()
    tutee = Tutee.objects.get(person = o)
    if tutee.asked == False and Question.objects.filter(person = o).count() == 1:
        q = Question.objects.get(person = o)
        q.delete()
    #After clicking submit
    print(Tutee.objects.get(person = o).asked)
    if request.method == "POST":
        #Get the user inputs
        question = request.POST.get('Question')
        class_id = request.POST.get('class')
        comments = request.POST.get('comments')
        #Store in model
        obj = Question() 
        obj.Question_text = question
        obj.Class_text = class_id
        obj.Comments_text = comments
        obj.person = Profile.objects.get(user=request.user)
        obj.save()
        o.save()
        return HttpResponseRedirect('tuteeing/results')
    context = {
         "classes": classes,
         "me": o,
         "user": tutee,
    }
    return render(request, 'tutee/main.html', context)

def results(request):
    #Grab all the questions
    questions = Question.objects.all()
    #Grab all the profiles
    people = Profile.objects.all()
    me = Profile.objects.get(user=request.user)
    question = questions.get(person=me)
    tutee = Tutee.objects.get(person=me)
    results = []
    #Check that a person took the class and is currently an active tutor 
    for p in people:
        if question.Class_text.upper() in p.classes:
            if p.activeStatus == True:
                #results.append(p)
                #0.015 for one mil
                if(math.sqrt((me.latitude - p.latitude)**2 + (me.longitude - p.longitude)**2) < 100):
                    results.append(p)
    context = {
        "people_list": people,
        "results": results,
    }
    return render(request, 'tutee/results.html', context)

def tutorProfile(request, tutor_id):
    tutor = Profile.objects.get(pk=tutor_id)
    context = {
         "tutor": tutor,
    }
    return render(request, 'tutee/tutorProfile.html', context)

def rating(request, tutor_id):
    #Get the tutor by the tutor_id set in results page
    tutor = Profile.objects.get(pk=tutor_id)
    #tutor.connection = Profile.objects.get(user=request.user).id
    me = Profile.objects.get(user=request.user)
    tutee = Tutee.objects.get(person=me)
    if not (str(Profile.objects.get(user=request.user).id) in tutor.questionsReceived) :
        if tutee.tuteeStatus != "rating":
            tutor.questionsReceived.append(Profile.objects.get(user=request.user).id)
            tutor.save()
    tutee = Tutee.objects.get(person=me)
    tutee.ratingPage = tutor_id
    if tutee.tuteeStatus == "none" and Question.objects.filter(person = me).count() == 1:
        tutee.tuteeStatus = "waiting"
        tutee.asked = True
    tutee.save()
    if request.method == "POST":
        #if user makes it to rating
        if 'submit' in request.POST:
            #Increment total rating 
            tutor.compositeRating = tutor.compositeRating + int(request.POST.get("rate"))
            #Increment times tutored
            tutor.timesTutored = tutor.timesTutored + 1
            #Calcuate the rating of the tutor
            tutor.tutorRate = tutor.compositeRating / tutor.timesTutored
            tutor.save()
            #Change status
            tutee.tuteeStatus = "none"
            tutee.asked = False
            tutee.save()
            #Return Home
        #if user decides to cancel the question
        elif 'cancel' in request.POST:
            tutee.tuteeStatus = "none"
            tutee.asked = False
            tutee.save()
            tutor.questionsReceived.remove(str(Profile.objects.get(user=request.user).id))
            tutor.save()
            question = Question.objects.get(person = me)
            question.delete()
        elif 'goResult' in request.POST:
            tutee.asked = False
            tutee.tuteeStatus = "none"
            tutee.save()
            return HttpResponseRedirect('/tuteeing/results')
        elif 'backHome' in request.POST:
            #delete question
            tutee.asked = False
            tutee.tuteeStatus = "none"
            tutee.save()
            question = Question.objects.get(person = me)
            question.delete()
        return HttpResponseRedirect('/home')
    context = {
        'tutor' : tutor,
        'tutee' : tutee,
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
    if 'enter' in request.POST:
        full_string = str(request.POST.get('Classes'))
        split_list = full_string.split(",")
        for i in split_list:
            if re.match(r"[A-Z]{2,4}[0-9]{4}$",i) and i not in o.classes:
                o.classes.append(i)
                o.save()
        return HttpResponseRedirect('newprofile2')
    if 'other' in request.POST:
        return HttpResponseRedirect('newprofile2.5')
    elif 'next' in request.POST:
        return HttpResponseRedirect('newprofile2.5')
    return render(request, 'login/newprofile2.html')

def newprofile2_5(request):
    o = Profile.objects.get(user = request.user)
    classes = o.classes
    context = {
        "classes": classes,
    }
    if 'back' in request.POST:
        return HttpResponseRedirect('newprofile2')
    elif 'next' in request.POST:
        return HttpResponseRedirect('newprofile2.75')
    return render(request, 'login/newprofile2.5.html', context)

def newprofile2_75(request):
    o = Profile.objects.get(user = request.user)
    if request.method == "POST":
        temp = float(request.POST.get('updateBalance'))  # person adds more money
        o.balance += round(round(temp * 100)) / 100
        o.save()
        return HttpResponseRedirect('newprofile3')
    return render(request, 'login/newprofile2.75.html')


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
    if request.method == "POST":
        temp = float(request.POST.get('updateBalance')) # person adds more money
        o.balance += round(round(temp * 100))/100
        o.save()
    context = {
         "user": o,
    }
    return render(request, 'login/userprofile.html', context)

def question(request, tutee_id):
    o = Profile.objects.get(user=request.user)
    tutee = Profile.objects.get(pk=tutee_id)
    question = Question.objects.get(person=tutee)
    context = {
        "user": o,
        "tutee": tutee,
        "question": question,
    }
    if request.method == "POST":
        if 'accept' in request.POST:
            o.connection = tutee_id
            o.save()
            return HttpResponseRedirect("/payment")
        elif 'decline' in request.POST:
            print(o.questionsReceived)
            print(Profile.objects.get(pk=tutee_id).id)
            o.questionsReceived.remove(str(Profile.objects.get(pk=tutee_id).id))
            o.save()
            t = Tutee.objects.get(person=tutee)
            t.tuteeStatus = "decline"
            t.save()
            return HttpResponseRedirect("/tutoring")
    return render(request, 'tutee/question.html', context)

def session(request):
    o = Profile.objects.get(user=request.user)
    tutee = Profile.objects.get(pk=o.connection)
    question = Question.objects.get(person=tutee)
    t = Tutee.objects.get(person=tutee)
    #notify tutee of acceptance
    t.tuteeStatus = "accept"
    t.save()
    context = {
        "user": o,
        "tutee": tutee,
        "question": question,

    }
    return render(request, 'tutor/session.html', context)

def payment(request):
    o = Profile.objects.get(user=request.user)
    tutee = Profile.objects.get(pk=o.connection)
    question = Question.objects.get(person=tutee)
    t = Tutee.objects.get(person=tutee)
    t.tuteeStatus = "accept"
    t.save()
    if request.method == "POST":

        # determine price for inputed time
        # hours = int(request.POST.get('hours'))
        # minutes = int(request.POST.get('minutes'))
        # seconds = int(request.POST.get('seconds'))
        # temp_minutes = (hours * 60) + minutes + (seconds / 60)
        # input_amount = (round(temp_minutes * 100))/100 # round to two decimals
        # input_amount = (input_amount / 5)
        # tutee.balance = tutee.balance - input_amount
        # o.balance = o.balance + input_amount
        o.activeStatus = True


        # determine price based on stopwatch
        amount = float(request.POST.get('Amount'))
        tutee.balance = tutee.balance - amount
        tutee.save()
        o.balance = o.balance + amount
        o.questionsReceived.remove(o.connection)
        o.connection = ""
        o.save()
        question.delete()


        # update tutee model

        t = Tutee.objects.get(person=tutee)
        t.tuteeStatus = "rating"
        t.timesTuteed = t.timesTuteed + 1
        t.save()

        return HttpResponseRedirect('tutoring')

    context = {
        "user": o,
        "tutee": tutee,
        # "amount": "0.00"
    }
    return render(request, 'tutor/payment.html', context)

def updateclasses(request):
    o = Profile.objects.get(user=request.user)
    if 'add' in request.POST:
        full_string = str(request.POST.get('Classes'))
        split_list = full_string.split(",")
        for i in split_list:
            if re.match(r"[A-Z]{2,4}[0-9]{4}$", i) and i not in o.classes:
                o.classes.append(i)
                o.save()
        return HttpResponseRedirect('updateclasses')
    if 'delete' in request.POST:
        full_string = str(request.POST.get('Classes'))
        if re.match(r"[A-Z]{2,4}[0-9]{4}$", full_string) and full_string in o.classes:
            o.classes.remove(request.POST.get('Classes'))
            o.save()
        return HttpResponseRedirect('updateclasses')
    if 'classes' in request.POST:
        return HttpResponseRedirect('classes')
    elif 'profile' in request.POST:
        return HttpResponseRedirect('userprofile')
    return render(request, 'login/addclasses.html')

def updatebio(request):
    o = Profile.objects.get(user = request.user)
    if 'update' in request.POST:
        o.bio = request.POST.get('Bio')
        o.save()
        return HttpResponseRedirect('userprofile')
    elif 'back' in request.POST:
        return HttpResponseRedirect('userprofile')
    return render(request, 'login/newbio.html')

def updatebalance(request):
    o = Profile.objects.get(user = request.user)
    if 'balance' in request.POST:
        temp = float(request.POST.get('updateBalance'))  # person adds more money
        o.balance += round(round(temp * 100)) / 100
        o.save()
        return HttpResponseRedirect('userprofile')
    if 'profile' in request.POST:
        return HttpResponseRedirect('userprofile')
    return render(request, 'login/addbalance.html')

def classes(request):
    o = Profile.objects.get(user=request.user)
    classes = o.classes
    context = {
        "classes": classes,
    }
    if 'back' in request.POST:
        return HttpResponseRedirect('userprofile')
    elif 'next' in request.POST:
        return HttpResponseRedirect('updateclasses')
    return render(request, 'login/classes.html', context)
