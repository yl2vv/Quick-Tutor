from django.db import models
from django.utils import timezone

class Tutor(models.Model):
    #from google API
    tutor_ID = models.CharField(max_length = 100) #not sure how long these IDs are


class Tutee(models.Model):
    #from google API
    tutee_ID = models.CharField(max_length = 100)

class Profile(models.Model):
    #change to true when the profile is created ?
    existing_profile = models.BooleanField(default = False)

    #from the google API
    new_user_ID = models.CharField(max_length = 100)
    new_user_email = models.CharField(max_length = 50)
    new_user_image = models.CharField()

    #additional information pulled from a new user profile
    date_created = models.DateTimeField(default = timezone.now)

