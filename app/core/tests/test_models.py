"""
Tests for models .
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_email_with_email_succesful(self):
        """Test if creating a user with email is succesful."""
        email = 'test@example.com'
        password = '123testpassword'
        user = get_user_model().objects.create_user(email=email,
                                                    password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
