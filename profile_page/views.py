from django.shortcuts import render
from .models import Profile

from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader

# class Profile(models.Model):
#     #change to true when the profile is created ?
#     existing_profile = models.BooleanField(default = False)
#
#     # change to get info from the google API
#     new_user_ID = models.CharField(max_length = 100)
#     new_user_email = models.CharField(max_length = 50)
#     new_user_image = models.CharField(max_length = 200)
#
#     #additional information pulled from a new user profile
#     date_created = models.DateTimeField(default = timezone.now)
#     #might want to add author = models.ForeignKey(User,on_delete=models.CASCADE)
#     name = models.CharField(max_length = 50)
#     gpa = models.CharField(max_length = 5)
#     phone_number = models.CharField(max_length = 12)
#     #shool_year and college should be pull down options
#     school_year = models.CharField(max_length = 3)
#     college = models.CharField(max_length = 50)
#     #classes_taken = #what kind of field should this be, ManytoMany
#     bio = models.TextField(max_length = 300)
#     def __str__(self):
#         # change this to what we actually want to return
#         return self.new_user_ID



#this view shows an already created profile (image, number of people tutored, etc. )
def newprofile(request):
    if request.method == "POST":
        newfirstname = request.POST.get('FirstName')
        newlastname = request.POST.get('LastName')
        newcomputingid = request.POST.get('ComputingID')
        newphonenumber = request.POST.get('PhoneNumber')
        newgpa = request.POST.get('GPA')
        newschoolyear = request.POST.get('SchoolYear')
        newbio = request.POST.get('Bio')

        o = Profile()
        o.firstname = newfirstname
        o.lastname = newlastname
        o.computingID = newcomputingid
        o.phone_number = newphonenumber
        o.gpa = newgpa
        o.school_year = newschoolyear
        o.bio = newbio

    return render(request, 'profile_form/newprofile.html')


def userprofile(request):
    return render(request, 'profile_form/userprofile.html')  # figure out how to pull data from newprofile