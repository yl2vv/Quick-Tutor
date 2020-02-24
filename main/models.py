from django.db import models
# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     pass
#     # add additional fields in here



class User(models.Model):
    userid = models.CharField(max_length=300)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    image = models.CharField(max_length=300)
    latitude = models.FloatField()
    longitude = models.FloatField()
    formCompleted = models.BooleanField()
