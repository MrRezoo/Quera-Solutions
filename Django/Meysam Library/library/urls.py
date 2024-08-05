"""config URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import borrow_book, get_book_users, return_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_book_users/<int:book_id>/', get_book_users, name='get_book_users'),
    path('borrow_book/<book_id>/<user_name>/', borrow_book, name='borrow_book'),
    path('return_book/<book_id>/', return_book, name='return_book'),
]
