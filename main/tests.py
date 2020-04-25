from django.test import TestCase
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import resolve
from allauth.socialaccount import models as socialmodel
from django.urls import reverse

from .models import Profile
from django.test.client import RequestFactory
from .views import loggedin
from django.contrib.auth.models import User, AnonymousUser


# Create your tests here.

class DummyTestCase(TestCase):
    def setUp(self):
        x = 1

    def test_dummy_test_case(self):
        self.assertEqual(1, 1)

class LogInViewTestCase(TestCase):

    def test_login_view(self):
        resolver = resolve('/')
        self.assertEqual(resolver.view_name, 'login:login')

class LoggedInViewTestCase(TestCase):

    def test_logged_in_view(self):
        resolver = resolve('/loggedIn')
        self.assertEqual(resolver.view_name, 'login:loggedin')


class HomeViewTestCase(TestCase):

    def test_home_view(self):
        resolver = resolve('/home')
        self.assertEqual(resolver.view_name, 'login:home')

class UserProfileViewTestCase(TestCase):

    def test_user_profile_view(self):
        resolver = resolve('/userprofile')
        self.assertEqual(resolver.view_name, 'login:userprofile')

class TutorTestCaseView(TestCase):

    def test_tutor_view(self):
        resolver = resolve('/tutoring')
        self.assertEqual(resolver.view_name, 'login:tutor')


class TuteeViewTestCase(TestCase):

    def test_tutee_view(self):
        resolver = resolve('/tuteeing')
        self.assertEqual(resolver.view_name, 'login:tutee')

class TuteeResultsViewTestCase(TestCase):

    def test_tutee_results_view(self):
        resolver = resolve('/tuteeing/results')
        self.assertEqual(resolver.view_name, 'login:results')



class LoginTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@quicktutor.com', password='password')

    def test_login_new_user(self):
        request = self.factory.get('/')
        request.user = self.user
        request.socialmodel = socialmodel.SocialAccount.objects.create(user=self.user)
        request.Profile = Profile.objects.create(user=self.user, Uid="1")
        # user = User.objects.get(username='testuser')
        # request.user = Profile.objects.create(user=user, firstname="test", lastname="user", formCompleted=True)
        response = loggedin(request)
        self.assertEqual(response.url, '/newprofile')

    def test_login_old_user(self):
        request = self.factory.get('/')
        request.user = self.user
        request.socialmodel = socialmodel.SocialAccount.objects.create(user=self.user)
        request.Profile = Profile.objects.create(user=self.user, Uid="1", formCompleted=True)
        response = loggedin(request)
        self.assertEqual(response.url, '/home')




