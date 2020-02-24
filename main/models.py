from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.utils import timezone
#for User ForeignKey from django.contrib.auth.models import User

class Tutor(models.Model):
#     # add additional fields in here
#     pass
# class CustomUser(AbstractUser):
    #from google API
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
    userid = models.CharField(max_length=300)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    image = models.CharField(max_length=300)
    latitude = models.FloatField()
    longitude = models.FloatField()
    formCompleted = models.BooleanField()
