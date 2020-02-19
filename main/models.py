from django.db import models

# Create your models here.


class User(models.Model):
    userid = models.CharField(max_length=300)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    image = models.CharField(max_length=300)
    location = models.FloatField()
    formCompleted = models.BooleanField()
