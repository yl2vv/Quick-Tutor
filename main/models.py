from django.db import models
from phone_field import PhoneField
from django.utils import timezone

class Tutor(models.Model):
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


class User(models.Model):
    #info from the API
    userid = models.CharField(max_length=300)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    image = models.CharField(max_length=300)
    latitude = models.FloatField()
    longitude = models.FloatField()
    formCompleted = models.BooleanField(default = False)

    #info from the profile form
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    phoneNumber = PhoneField(blank = True, help_text = 'Mobile phone number')
    computingID = models.CharField(max_length =7)
    schoolYear = models.IntegerField()
    classes = models.CharField(max_length=200)
    gpa = models.CharField(max_length =4)
    bio = models.TextField(max_length = 300)