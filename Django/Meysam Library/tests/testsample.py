import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client

# Create your tests here.
from app.models import Book


class SimpleTest(TestCase):
    def setUp(self):
        try:
            self.user_1 = User.objects.get(email='user_1@test.me')
        except User.DoesNotExist:
            self.user_1 = User.objects.create(
                email='user_1@test.me',
                first_name='user',
                last_name='1',
                username='user_1'
            )
        try:
            self.user_2 = User.objects.get(email='user_2@test.me')
        except User.DoesNotExist:
            self.user_2 = User.objects.create(
                email='user_2@test.me',
                first_name='user',
                last_name='2',
                username='user_2'
            )
        try:
            self.book_1 = Book.objects.get(id=1)
        except Book.DoesNotExist:
            self.book_1 = Book.objects.create(
                name='book_1',
                author='a',
                isbn='1'
            )
        try:
            self.book_2 = Book.objects.get(id=2)
        except Book.DoesNotExist:
            self.book_2 = Book.objects.create(
                name='book_2',
                author='b',
                isbn='2'
            )
        try:
            self.book_3 = Book.objects.get(id=3)
        except Book.DoesNotExist:
            self.book_3 = Book.objects.create(
                name='book_3',
                author='c',
                isbn='3'
            )
        self.client = Client()

    def test_borrow_book(self):
        response = self.client.get('/borrow_book/1/abc/')
        self.assertEqual(json.loads(str(response.content.decode('utf-8'))), {"status": 3})
        response = self.client.get('/borrow_book/1/user_1/')
        self.assertEqual(json.loads(str(response.content.decode('utf-8'))), {"status": 0})

    def test_return_book(self):
        response = self.client.get('/return_book/4/')
        self.assertEqual(json.loads(str(response.content.decode('utf-8'))), {"status": 2})
        response = self.client.get('/return_book/2/')
        self.assertEqual(json.loads(str(response.content.decode('utf-8'))), {"status": 1})
