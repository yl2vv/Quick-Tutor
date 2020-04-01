from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login, name='login'),
    path('loggedIn', views.loggedin, name='loggedin'),
    path('home', views.home, name = 'home'),
    path('tutoring', views.tutoring, name='tutor'),
    path('tuteeing', views.tuteeing, name='tutee'),
    path('newprofile',views.newprofile,name='newprofile'),
    path('newprofile1',views.newprofile1,name='newprofile1'),
    path('newprofile2',views.newprofile2,name='newprofile2'),
    path('newprofile3',views.newprofile3, name = 'newprofile3'),
    path('userprofile',views.userprofile,name='userprofile')
]