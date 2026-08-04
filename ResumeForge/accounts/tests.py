from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .services import AuthService

class AccountsAuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'hr_test_user'
        self.password = 'SecurePassword123!'
        self.email = 'hr_test@example.com'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email=self.email
        )

    def test_auth_service_authenticate(self):
        """
        Tests that AuthService properly validates credentials.
        """
        user = AuthService.authenticate_user(None, self.username, self.password)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, self.username)

        invalid_user = AuthService.authenticate_user(None, self.username, 'wrongpassword')
        self.assertIsNone(invalid_user)

    def test_login_view_get(self):
        """
        Tests that the login view renders correctly.
        """
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_login_view_post_success(self):
        """
        Tests login form submission with valid credentials.
        """
        response = self.client.post(reverse('accounts:login'), {
            'username': self.username,
            'password': self.password,
            'remember_me': False,
        })
        self.assertRedirects(response, reverse('dashboard:home'))

    def test_login_view_post_failure(self):
        """
        Tests login form submission with invalid credentials.
        """
        response = self.client.post(reverse('accounts:login'), {
            'username': self.username,
            'password': 'WrongPassword',
            'remember_me': False,
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_registration_view_post_success(self):
        """
        Tests registering a new unique user.
        """
        response = self.client.post(reverse('accounts:register'), {
            'username': 'new_hr_user',
            'email': 'new_hr@example.com',
            'password1': 'NewSecurePass123!',
            'password2': 'NewSecurePass123!',
        })
        self.assertRedirects(response, reverse('dashboard:home'))
        self.assertTrue(User.objects.filter(username='new_hr_user').exists())

    def test_registration_view_post_duplicate_username(self):
        """
        Tests registration clean validator blocks duplicate usernames.
        """
        response = self.client.post(reverse('accounts:register'), {
            'username': self.username,
            'email': 'different_email@example.com',
            'password1': 'NewSecurePass123!',
            'password2': 'NewSecurePass123!',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This username is already taken.')

    def test_logout_redirect(self):
        """
        Tests session termination and redirection.
        """
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('accounts:logout'))
        self.assertRedirects(response, reverse('accounts:login'))

    def test_middleware_redirect_unauthenticated(self):
        """
        Tests that the LoginRequiredMiddleware redirects anonymous users.
        """
        # A route that is not exempt should redirect
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('accounts:login')))
