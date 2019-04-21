from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTest(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Create user with email
        """
        email = 'jeff@astor.io'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Test that user has normalized email
        """
        email = 'jeff@ASTOR.io'
        user = get_user_model().objects.create_user(email, 'testpass123')

        self.assertEqual(user.email, email.lower())

    def test_user_invalid_email(self):
        """Test creating user with no email causes error"""
        with self.assertRaises(ValueError):
            email = None
            user = get_user_model().objects.create_user(email, 'testpass123')
            return user

    def test_can_create_super_user(self):
        """
        Test that user can be created with is_staff
        and is_super_user both True
        """
        user = get_user_model().objects.create_superuser(
            'jeff@astor.io',
            'supersecretpassword'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
