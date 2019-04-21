from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='jeff@astor.io',
            password='testpass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@astor.io',
            password='supersecretpassword',
            name='Test User Full Name'
        )

    def test_users_listed(self):
        """
        Test that users are listed on user page
        """
        # make it easy to find the url the the admin changelist
        url = reverse('admin:core_user_changelist')
        # send a get request to the url
        res = self.client.get(url)
        # checks that the http response was 200
        # looks at content of res and find the contents
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """
        Test that the user change page works
        """
        url = reverse('admin:core_user_change', args=[self.user.id])
        # admin/core/user/$user.id
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """
        Test that user page can be created
        """
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
