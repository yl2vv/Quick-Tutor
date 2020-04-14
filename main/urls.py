from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login, name='login'),
    path('loggedIn', views.loggedin, name='loggedin'),
    path('home', views.home, name = 'home'),
    path('tutoring', views.tutoring, name='tutor'),
    path('tuteeing', views.tuteeing, name='tutee'),
    path('tuteeing/results', views.results, name='results'),
    path('tuteeing/results/<tutor_id>', views.tutorProfile, name='tutorProfile'),
    path('tuteeing/results/rating/<tutor_id>', views.rating, name='rating'),
    path('newprofile',views.newprofile,name='newprofile'),
    path('newprofile1',views.newprofile1,name='newprofile1'),
    path('newprofile2',views.newprofile2,name='newprofile2'),
    path('newprofile2.25',views.newprofile2_25,name = 'newprofile2_25'),
    path('newprofile2.5',views.newprofile2_5,name = 'newprofile2_5'),
    path('newprofile3',views.newprofile3, name = 'newprofile3'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('question',views.question,name='question'),
    path('session', views.session, name='session'),
    path('payment', views.payment, name='payment'),
    path('updateclasses', views.updateclasses, name = 'updateclasses'),
    path('updatebio',views.updatebio,name = 'updatebio'),
    path('updatebalance',views.updatebalance, name = 'updatebalance')
]