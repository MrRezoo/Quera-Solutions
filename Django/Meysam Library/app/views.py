from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Book, Borrowing


def get_book_users(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    borrowings = Borrowing.objects.filter(book=book).order_by('date')
    response_data = [
        {"username": borrowing.user.username, "date": borrowing.date.isoformat()}
        for borrowing in borrowings
    ]
    return JsonResponse(response_data, safe=False)


def borrow_book(request, book_id, user_name):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return JsonResponse({"status": 3})

    try:
        user = User.objects.get(username=user_name)
    except User.DoesNotExist:
        return JsonResponse({"status": 3})

    if book.user_borrowed:
        return JsonResponse({"status": 1})

    if Book.objects.filter(user_borrowed=user).exists():
        return JsonResponse({"status": 2})

    book.borrow_book(user)
    return JsonResponse({"status": 0})


def return_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return JsonResponse({"status": 2})

    if not book.user_borrowed:
        return JsonResponse({"status": 1})

    book.return_book()
    return JsonResponse({"status": 0})
