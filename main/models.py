from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_mysql.models import ListCharField

class Profile(models.Model):
    STUDENT = 1
    TEACHER = 2
    SUPERVISOR = 3
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (SUPERVISOR, 'Supervisor'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Uid = models.IntegerField(default=0)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    email = models.EmailField(blank=True)
    image = models.ImageField(blank=True)
    #latitude = models.FloatField()
    #longitude = models.FloatField()
    formCompleted = models.BooleanField(default=False)
    classes = ListCharField(base_field=models.CharField(max_length=15),size=15,max_length= 240,blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



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


