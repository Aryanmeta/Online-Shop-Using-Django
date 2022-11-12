from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignUpPageTest(TestCase):
    username = 'username'
    email = 'username@gmail.com'

    def test_signup_page_by_url_name(self):
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_by_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_template_used(self):
<<<<<<< HEAD
        response = self.client.get(reverse('account_signup'))
=======
        response = self.client.get(reverse('signup'))
>>>>>>> refs/remotes/origin/main
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_signup_page_content(self):
        response = self.client.get(reverse('account_signup'))
        self.assertContains(response, 'Sign Up')

    def test_signup_form(self):
        get_user_model().objects.create_user(
            self.username,
            self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
