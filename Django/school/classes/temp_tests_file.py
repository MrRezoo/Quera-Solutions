from django.test import TestCase
from rest_framework.exceptions import ValidationError

from classes.serializers import ClassroomSerializer


class SerializerTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.valid_data = {'capacity': 5, 'area': 10, 'name': 'Room A', 'department': 'Science'}
        cls.invalid_capacity_data = {'capacity': 4, 'area': 10, 'name': 'Room A', 'department': 'Science'}
        cls.invalid_area_data = {'capacity': 10, 'area': -1, 'name': 'Room B', 'department': 'Arts'}

    def test_valid_capacity(self):
        serializer = ClassroomSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_capacity(self):
        serializer = ClassroomSerializer(data=self.invalid_capacity_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_valid_area(self):
        serializer = ClassroomSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_area(self):
        serializer = ClassroomSerializer(data=self.invalid_area_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
