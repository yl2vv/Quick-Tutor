from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Question


def question(request):
    #Add data to models
    print("hello")
    if request.method == "POST":
        #Get the user inputs
        question = request.POST.get('Question')
        class_id = request.POST.get('class')
        file_upload = request.POST.get('upload')
        comments = request.POST.get('comments')
        print(question)
        #Store in model
        obj = Question() 
        obj.Question_text = question
        obj.Class_text = class_id
        obj.File_upload = file_upload
        obj.Comments_text = comments
        obj.save()
    context = {}
    return render(request, 'main/question.html', context)

def results(request):
    queryset = Question.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'main/results.html', context)