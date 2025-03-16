#################################################################
# file: trackingapp/tests.py 
#################################################################
from django.test import TestCase, Client
from django.urls import reverse
from .models import User

class SimpleTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a test user
        self.test_user = User.objects.create_user(username='testuser', password='12345', role='STUDENT')

    def test_homepage_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        login_success = self.client.login(username='testuser', password='12345')
        # MFA does not do in-depth testing here, just verify that the username and password are correct.
        self.assertTrue(login_success)
