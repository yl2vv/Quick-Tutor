from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_mysql.models import ListCharField
from django.conf import settings
from allauth import app_settings
from allauth.account.models import EmailAddress
from allauth.account.utils import get_next_redirect_url, setup_user_email
from allauth.utils import get_user_model



class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50,blank=True)
    lastname = models.CharField(max_length=50,blank=True)
    Uid = models.CharField(max_length=100,blank=True)
    computingID = models.CharField(max_length=10,blank=True)
    email = models.EmailField(blank=True)
    phoneNumber = models.CharField(max_length=50,blank=True)
    image = models.CharField(max_length=300,blank=True)
    latitude = models.FloatField(default=0.0,blank=True)
    longitude = models.FloatField(default=0.0,blank=True)
    formCompleted = models.BooleanField(default=False)
    gpa = models.FloatField(default=0.0,blank=True)
    schoolYear = models.IntegerField(default=0,blank=True)
    classes = ListCharField(base_field=models.CharField(max_length=15),size=15,max_length= 240,blank=True)
    bio = models.CharField(max_length=500,blank=True)
    activeStatus = models.BooleanField(default=False) #Are they an active tutor
    connection = models.CharField(max_length=50,blank=True) #Who they are tutoring
    tutorRate = models.FloatField(default=0.0,blank=True) #the rating of tutor
    compositeRating = models.IntegerField(default=0, blank=True) #total score recieved to calculate rating
    timesTutored = models.IntegerField(default=0,blank=True) #the number of times tutored
    timesTutteed = models.IntegerField(default=0,blank=True) #the number of times got help
    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


class Question(models.Model):
    Question_text = models.CharField(default='',max_length=200)
    Class_text = models.CharField(default='',max_length=200)
    Comments_text = models.CharField(default='',max_length=10000)
    File_upload = models.ImageField()
    person = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.Question_text

# class User(models.Model):
#     userid = models.CharField(max_length=300)
#     name = models.CharField(max_length=50)
#     email = models.EmailField()
#     image = models.CharField(max_length=300)
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     formCompleted = models.BooleanField()

class Tutor(models.Model):
    #from google API
    tutor_ID = models.CharField(max_length = 100) #not sure how long these IDs are

    def __str__(self):
        #change this to what we actually want to return
        return self.tutor_ID


class Tutee(models.Model):
    #from google API
    tutee_ID = models.CharField(max_length = 100)
    def __str__(self):
        # change this to what we actually want to return
        return self.tutee_ID