from django.db import models

# Create your models here.
class Question(models.Model):
    Question_text = models.CharField(max_length=200)
    Class_text = models.CharField(max_length=200)
    Comments_text = models.CharField(max_length=10000)
    File_upload = models.ImageField()
    def __str__(self):
        return self.Question_text