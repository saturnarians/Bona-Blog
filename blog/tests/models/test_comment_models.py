# Core Django imports.
from django.test import TestCase

# Third-party Django app imports.
from model_bakery import baker

# Blog application imports.
from blog.models import Article
from blog.models.comment_models import Comment


class CommentTestCase(TestCase):
    """
      Class to test the Blog model.
    """

    def setUp(self):
        """
          Set up all the tests using model_bakery.
        """
        self.article = baker.make(_model=Article, body="Test")
        self.comment = baker.make(Comment, article=self.article)

    def test_if_comment_returns_the_right_user(self):
        self.assertEqual(
            self.comment.__str__(),
            f"Comment by {self.comment.name} on {self.comment.article}")
