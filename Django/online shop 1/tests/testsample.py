import json

from django.test import TestCase
from django.test.client import Client
from django import forms

from shop.models import Color, Product


class ShopTest(TestCase):
    def setUp(self):
        c1 = Color.objects.create(name="red")
        c2 = Color.objects.create(name="blue")

        p1 = Product.objects.create(name='iphone6')
        p1.colors_available.add(c1, c2)
        p1.save()
        p1.delete()

        p2 = Product.objects.create(name='JBL')
        p2.colors_available.add(c1)
        p2.save()

    def test_form_fields_availability_check(self):
        c = Client()
        response = c.get('/shop/cart')
        self.assertEqual(response.status_code, 200)
        fields = []
        for field in response.context['form'].fields:
            fields.append(field)

        self.assertListEqual(sorted(fields),
                             sorted(['number_2', 'color_2']))
