from django.test import TestCase

from store import queries


class TestTasks(TestCase):
    fixtures = ('store',)

    def test_sum_of_income(self):
        solution = 61160
        answer = queries.sum_of_income("2023-07-01", "2023-07-30")
        self.assertEqual(solution, answer)
