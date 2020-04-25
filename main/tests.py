from django.test import TestCase
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import resolve

from .models import Profile
from django.test.client import RequestFactory
from .views import loggedin
from django.contrib.auth.models import User


# Create your tests here.

class DummyTestCase(TestCase):
    def setUp(self):
        x = 1

    def test_dummy_test_case(self):
        self.assertEqual(1, 1)


class HomeTestCase(TestCase):

    def test_home(self):
        resolver = resolve('/home')
        self.assertEqual(resolver.view_name, 'login:home')


class TutorTestCase(TestCase):

    def test_tutor(self):
        resolver = resolve('/tutoring')
        self.assertEqual(resolver.view_name, 'login:tutor')


class TuteeTestCase(TestCase):

    def test_tutee(self):
        resolver = resolve('/tuteeing')
        self.assertEqual(resolver.view_name, 'login:tutee')

# class LoginTestCase(TestCase):
#     def setUp(self) -> None:
#         self.factory = RequestFactory()
#
#     def test_login(self):
#         request = self.factory.get('')
#         user = User.objects.create_user('andrew', 'andrewdowning231@gmail.com')
#         request.user = user
#         response = loggedin(request)
#         self.assertEqual(response.status_code, 200)


