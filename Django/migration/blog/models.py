from django.db import models
from django.utils import timezone

from config import settings


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'publish'),
    )
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
