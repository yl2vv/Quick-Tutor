from django.urls import path

from . import views

app_name = 'question'
urlpatterns = [
    path('question/', views.question, name='question'),
    path('results/', views.results, name='results')
]