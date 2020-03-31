from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login, name='login'),
    path('loggedIn', views.loggedin, name='loggedin'),
    path('home', views.home, name = 'home'),
    path('tutoring', views.tutoring, name='tutor'),
    path('tuteeing', views.tuteeing, name='tutee'),
    path('tuteeing/results', views.results, name='tuteeResults'),
    path('tuteeing/results/rating', views.rating, name='rating'),
    path('newprofile',views.newprofile,name='newprofile'),
    path('userprofile',views.userprofile,name='userprofile')
]