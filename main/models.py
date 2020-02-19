from django.db import models
from django.utils import timezone
#for User ForeignKey from django.contrib.auth.models import User

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

class Profile(models.Model):
    #change to true when the profile is created ?
    existing_profile = models.BooleanField(default = False)

    # change to get info from the google API
    new_user_ID = models.CharField(max_length = 100)
    new_user_email = models.CharField(max_length = 50)
    new_user_image = models.CharField(max_length = 200)

    #additional information pulled from a new user profile
    date_created = models.DateTimeField(default = timezone.now)
    #might want to add author = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    gpa = models.CharField(max_length = 5)
    phone_number = models.CharField(max_length = 12)
    #shool_year and college should be pull down options
    school_year = models.CharField(max_length = 3)
    college = models.CharField(max_length = 50)
    #classes_taken = #what kind of field should this be, ManytoMany
    bio = models.TextField(max_length = 300)
    def __str__(self):
        # change this to what we actually want to return
        return self.new_user_ID