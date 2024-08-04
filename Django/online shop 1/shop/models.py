from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    colors_available = models.ManyToManyField(Color)

    def __str__(self):
        return self.name
