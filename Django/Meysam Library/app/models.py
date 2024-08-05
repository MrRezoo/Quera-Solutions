from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    user_borrowed = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=30)
    isbn = models.CharField(max_length=80)

    def borrow_book(self, user):
        if self.user_borrowed is not None:
            return False

        self.user_borrowed = user

        borrowing = Borrowing()
        borrowing.book = self
        borrowing.user = self.user_borrowed
        borrowing.save()

        self.save()

    def return_book(self):
        self.user_borrowed = None
        self.save()

    def __str__(self):
        return self.name


class Borrowing(models.Model):
    """
    Class representing the borrowing relationship.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
