from django.urls import reverse

from __tests__.setups.api_test_case_with_auth import APITestCaseWithAuthentication


class CreateClassroomTests(APITestCaseWithAuthentication):
    def setUp(self) -> None:
        super().setUp()

        self.API_URL = reverse('create_classroom')

    def test_validate_color_id(self):
        response = self.client.post(
            self.API_URL,
            data={
                'name': 'Aula 1',
                'color_id': 'color id'
            },
            format='json'
        )

        self.assertIsNotNone(response.data.get('validation_errors'))

