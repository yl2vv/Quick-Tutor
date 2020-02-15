from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login, name='login'),
    path('loggedIn', views.loggedin, name='loggedin'),
    path('home', views.home, name = 'home')
]