from django.forms import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_new_user_with_email(self):
        """"
        tests creating a new user with email
        """
        email = 'test_id@domain.com'
        password = 'Test_password@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_with_normalized_email(self):
        """
        tests normalized email for new user
        """
        email = 'test_ID007@Domain.com'
        user = get_user_model().objects.create_user(email, 'test#123')
        self.assertEqual(user.email, 'test_ID007@domain.com')

    def test_new_user_with_invalid_email(self):
        """
        tests invalid email for new user
        """
        with self.assertRaises(ValidationError):
            get_user_model().objects.create_user('abc.com', 'xyz')

    def test_create_new_superuser(self):
        """
        tests creating a new superuser
        """
        user = get_user_model().objects.create_superuser(
            'test_id@domain.com',
            'password123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        