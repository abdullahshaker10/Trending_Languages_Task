from rest_framework.test import APIClient, APITestCase
from django.urls import reverse


class TestlanguageAPIView(APITestCase):
    def setUp(self) -> None:
        self.languages_number = 100
        self.client = APIClient()

    def test_get_languages_api(self):
        response = self.client.get(
            reverse(
                "languages:get_trending_languages",
                args=(self.languages_number,),
            )
        )
        self.assertEqual(response.status_code, 200)
