import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionModelsTests(TestCase):
    def test_was_published(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_data=time)
        self.assertIs(future_question.was_published_recently(), False)