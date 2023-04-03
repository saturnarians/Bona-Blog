# Core Django imports.
from django.contrib.auth.models import User
from django.test import TestCase

# Third-party Django app imports.
from model_bakery import baker

# Blog application imports.


class AuthorProfileTestCase(TestCase):
    """
      Class to test the AuthorProfile Model.
    """

    def setUp(self):
        """
         Set up all the tests using model_bakery.
        """
        self.user = baker.make(User)

    def test_if_user_profile_returns_the_correct_username(self):
        self.assertEqual(self.user.profile.__str__(),
                         f"{self.user.username}'s Profile")

    def test_if_user_profile_returns_default_picture_if_user_does_not_upload_picture(self):
        self.assertEqual(self.user.profile.image.name, "profile-pic-default.jpg")