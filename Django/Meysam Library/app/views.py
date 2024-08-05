from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from app.models import Book, Borrowing


def get_book_users(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    borrowings = Borrowing.objects.filter(book=book).select_related('user')

    response_data = [
        {"username": borrowing.user.username, "date": borrowing.date.isoformat()}
        for borrowing in borrowings
    ]

    return JsonResponse(response_data, safe=False)


def borrow_book(request, book_id, user_name):
    book = Book.objects.filter(id=book_id).first()
    user = User.objects.filter(username=user_name).first()

    if book is None or user is None:
        return JsonResponse({"status": 3})

    if book.user_borrowed is not None:
        return JsonResponse({"status": 1})

    if Borrowing.objects.filter(book=book, user=user).exists():
        return JsonResponse({"status": 2})
    try:
        book.borrow_book(user)
    except:
        return JsonResponse({"status": 4})

    return JsonResponse({"status": 0})


def return_book(request, book_id):
    book = Book.objects.filter(id=book_id).first()

    if book is None:
        return JsonResponse({"status": 2})
    if book.user_borrowed is None:
        return JsonResponse({"status": 1})

    try:
        book.return_book()
    except:
        return JsonResponse({"status": 3})

    return JsonResponse({"status": 0})
