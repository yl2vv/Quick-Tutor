from django.test import TestCase
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import resolve

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
