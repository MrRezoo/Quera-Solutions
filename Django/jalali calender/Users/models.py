import jdatetime
from django.db import models
from django_jalali.db.models import jDateField, jDateTimeField


class CustomUser(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
    username = models.CharField(max_length=256)
    full_name = models.CharField(max_length=256)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    national_code = models.CharField(max_length=10)
    birthday_date = jDateField()
    ceremony_datetime = jDateTimeField()
    country = models.CharField(max_length=4, default="Iran")

    def get_first_and_last_name(self):
        split_name = self.full_name.split(" ")
        return {"first_name": split_name[0], "last_name": split_name[1]}

    def get_age(self):
        today = jdatetime.datetime.now().date()
        return today.year - self.birthday_date.year - ((today.month, today.day) < (self.birthday_date.month, self.birthday_date.day))

    def is_birthday(self):
        today = jdatetime.datetime.now().date()
        return today.month == self.birthday_date.month and today.day == self.birthday_date.day