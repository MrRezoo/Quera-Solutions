from unittest import TestCase

from rest_framework.test import APIClient


class TestViews(TestCase):
    databases = ['hospitals', 'companies', 'default']

    def test_invalid_input_company(self):
        client = APIClient()
        response = client.post('/get_company/', data={'name': None}, format='json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_input_hospital(self):
        client = APIClient()
        response = client.post('/get_hospital/', data={'name': None}, format='json')
        self.assertEqual(response.status_code, 400)
