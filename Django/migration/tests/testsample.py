from django.test import TestCase
from django.utils import timezone

from freezegun import freeze_time

from account.models import User
from blog.models import Article


class MigrationTest(TestCase):

    def test_article_model_is_correct(self):
        farhad = User.objects.create_user(username="Farhad", password="temp_pass")
        info = {
            "author": farhad,
            "title": "test_title",
            "body": "test_body",
        }
        try:
            with freeze_time("2012-01-14 12:00:01"):
                Article.objects.create(**info)
                article_create_datetime = timezone.now()
        except Exception:
            self.fail("Person model is not properly implemented")
