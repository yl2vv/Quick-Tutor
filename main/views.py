from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def question(request):
    return render(request, 'main/question.html')