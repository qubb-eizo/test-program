from django.urls import reverse
from django.test import TestCase, Client

from account.models import User

CREDENTIALS = {
    'username': 'AdminUser',
    'first_name': 'AdminUserFirst',
    'last_name': 'AdminUserLast',
    'email': 'email@admin.com',
    'password1': 'qwerTY123!',
    'password2': 'qwerTY123!',
}


class RegistrationTest(TestCase):

    def setUp(self):
        self.client = Client()

    def _register(self, credentials):
        url = reverse('account:registration')
        return self.client.post(url, credentials)

    def test_registration(self):
        user_count = User.objects.count()
        response = self._register(CREDENTIALS)
        assert response.url.startwith(reverse('account:login'))
        assert response.status_code == 302
        assert User.objects.count() == (user_count + 1)

    def test_login(self):
        self._register(CREDENTIALS)
        self.client.login(username='AdminUser', password='qwerT123!')
        response = self.client.get(reverse('account:profile'))
        assert response.status_code == 200
        assert 'Update' in response.content.decode()
