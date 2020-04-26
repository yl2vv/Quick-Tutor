from django.test import TestCase
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import resolve
from allauth.socialaccount import models as socialmodel
from django.urls import reverse

from .models import Profile, Question, Tutee
from django.test.client import RequestFactory
from .views import loggedin, tuteeing, results
from django.contrib.auth.models import User


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

class NewProfileTestCase(TestCase):

    def test_new_profile_view(self):
        resolver = resolve('/newprofile')
        self.assertEqual(resolver.view_name, 'login:newprofile')

class NewProfile1TestCase(TestCase):

    def test_new_profile1_view(self):
        resolver = resolve('/newprofile1')
        self.assertEqual(resolver.view_name, 'login:newprofile1')

class NewProfile2TestCase(TestCase):

    def test_new_profile2_view(self):
        resolver = resolve('/newprofile2')
        self.assertEqual(resolver.view_name, 'login:newprofile2')

class NewProfile3TestCase(TestCase):

    def test_new_profile3_view(self):
        resolver = resolve('/newprofile3')
        self.assertEqual(resolver.view_name, 'login:newprofile3')

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


class TuteeingTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@quicktutor.com', password='password')

    # def test_tuteeing(self):
    #     request = self.factory.get('/home')
    #     request.user = self.user
    #     request.socialmodel = socialmodel.SocialAccount.objects.create(user=self.user)
    #     request.Profile = Profile.objects.create(user=self.user, Uid="1", formCompleted=True)
    #     response = tuteeing(request)
    #     self.assertEqual(response.url, '/tuteeing/results')

    # def test_results(self):
    #     request = self.factory.get('/tutee')
    #     request.user = self.user
    #     request.socialmodel = socialmodel.SocialAccount.objects.create(user=self.user)
    #     request.Profile = Profile.objects.create(user=self.user, Uid="1", classes="[CS3240]", formCompleted=True)
    #     request.Question = Question.objects.create(Question_text="???", Class_text="CS3240", person=request.Profile)
    #     request.Tutee = Tutee.objects.create(person=request.Profile, tuteeStatus="waiting", asked=True)
    #     response = results(request)
    #     self.assertEqual(response.url, '/tutee/results')