from django.test import TestCase
from cabin import queries
from django.db.models.query import QuerySet


class SampleTests(TestCase):
    fixtures = ['sample_test_fixture.json']

    def test_1(self):
        q = queries.query_1()
        self.assertEqual(q['income'], 57500)

    def test_2(self):
        q = queries.query_2(3)
        self.assertEqual(q['payment_sum'], 9000)

    def test_3(self):
        q = queries.query_3()
        self.assertEqual(q, 2)

