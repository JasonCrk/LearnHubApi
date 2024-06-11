from rest_framework.test import APITestCase

from apps.user.models import UserAccount

from ..constants import TEST_PASSWORD
from ..factories.user_account import UserAccountFactory


class APITestCaseWithAuthentication(APITestCase):
    LOGIN_API_URL = '/api/v1/auth/jwt/create/'

    def setUp(self):
        self.auth_user: UserAccount = UserAccountFactory.create(password=TEST_PASSWORD)

        response = self.client.post(
            self.LOGIN_API_URL,
            {
                'email': self.auth_user.email,
                'password': TEST_PASSWORD
            },
            format='json'
        )

        print(response.get('data'))

        self.access_token = response.data.get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        return super().setUp()
