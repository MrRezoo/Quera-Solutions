from django.test import TestCase
from django.contrib import admin

from Users.models import CustomUser
from Users.forms import CustomUserForm
from django_jalali.db import models as jmodels

from freezegun import freeze_time

import jdatetime


class TestFoo(TestCase):
    def setUp(self):
        self.custom_user_admin = admin.site._registry.get(CustomUser)

        date = jmodels.jdatetime.date(1395, 1, 1)
        datetime = jmodels.jdatetime.datetime(1395, 2, 12, 12, 12, 12)
        self.user1 = CustomUser.objects.create(username='isara', full_name='Sara Ahmadi', gender='F', national_code='5110126432', birthday_date=date, ceremony_datetime=datetime)
        
    def test_models_are_registered_admin(self):
        self.assertTrue(CustomUser in admin.site._registry)

    def test_model_date(self):
        self.assertIsInstance(self.user1.birthday_date, jmodels.jdatetime.date)
    
    def test_model_gender(self):
        self.assertEqual(self.user1.gender, 'F')
    
    @freeze_time("2032-01-01")
    def test_model_get_age(self):
        print(self.user1.get_age())
        print(self.user1.is_birthday())
        self.assertEqual(self.user1.get_age(), 15)

    def test_form_is_valid(self):
        form_data = {
            'username': 'Mammad',
            'gender': 'M',
            'country': 'Iran',
            'full_name': 'Mohammad Mohammadi',
            'national_code': '4486934768',
            'birthday_date': '1367-12-12',
            'ceremony_datetime': '1400-10-10 12:12:12',
        }
        form = CustomUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_wrong_gender(self):
        form_data = {
            'username': 'Mammad',
            'gender': 'Q',
            'country': 'Iran',
            'full_name': 'Mohammad Mohammadi',
            'national_code': '4486934768',
            'birthday_date': '1367-12-12',
            'ceremony_datetime': '1400-10-10 12:12:12',
        }
        form = CustomUserForm(data=form_data)
        self.assertFalse(form.is_valid())