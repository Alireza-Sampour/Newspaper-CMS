# pages/tests.py
from django.contrib.auth.models import User
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.forms import EmailField


class HomePageTests(SimpleTestCase):
    
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):

    username = 'test_user1'
    correct_email = 'test_user@test.com'
    incorrect_email = '1@1.c'
    strong_password = 'QqqHJ1UNjV2cVGcq'
    weak_password = '1234'

    def test_signup_page_status_code(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        User.objects.create_user(self.username, self.correct_email, self.strong_password)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(User.objects.all()[0].username, self.username)
        self.assertEqual(User.objects.all()[0].email, self.correct_email)

    def test_form_with_correct_data(self):
        form = CustomUserCreationForm(data={
            'username': self.username,
            'password1': self.strong_password,
            'password2': self.strong_password,
            'email': self.correct_email
        })
        self.assertTrue(form.is_valid())
    
    def test_form_with_weak_password(self):
        form = CustomUserCreationForm(data={
            'username': self.username,
            'password1': self.weak_password,
            'password2': self.weak_password,
            'email' : self.correct_email
        })
        self.assertFalse(form.is_valid())

    def test_form_with_different_password(self):
        form = CustomUserCreationForm(data={
            'username': self.username,
            'password1': self.weak_password,
            'password2': self.strong_password,
            'email': self.correct_email
        })
        self.assertFalse(form.is_valid())

    def test_form_with_wrong_email_format(self):
        form = CustomUserCreationForm(data={
            'username': self.username,
            'password1': self.strong_password,
            'password2': self.strong_password,
            'email': self.incorrect_email
        })
        self.assertFalse(form.is_valid())
        self.assertFieldOutput(EmailField, {self.correct_email: self.correct_email}, {self.incorrect_email: ['Enter a valid email address.']})

    def test_username_help_text(self):
        form = CustomUserCreationForm()
        self.assertEqual(form.fields['username'].help_text, 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
