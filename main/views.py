from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Question, People


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
    questions = Question.objects.all()
    people = People.objects.all()
    results = []
    for p in people:
        if questions.reverse()[0].Class_text.upper() in p.class_id.upper():
            if p.status == True:
                results.append(p)
    context = {
        "questions_list": questions,
        "people_list": people,
        "results": results,
    }
    return render(request, 'main/results.html', context)