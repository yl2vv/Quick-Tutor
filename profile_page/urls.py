from django.urls import path

from . import views

app_name = 'profile_page'
urlpatterns = [
    path('userprofile/',views.userprofile,name='userprofile')
]