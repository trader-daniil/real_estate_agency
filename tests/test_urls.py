from django.test import Client, TestCase
from django.urls import reverse

HOMEPAGE = reverse('main_page')
SEARCH_FLAT_URL = reverse('search_flats_page')
TEMPLATE_FILENAME = 'flats_list.html'


class PropertyUrlTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()

    def test_url_exists_at_desired_location(self):
        """Проверка url и статуса ответа"""
        guest_client = PropertyUrlTest.guest_client
        self.assertEqual(
            guest_client.get(HOMEPAGE).status_code,
            200,
        )
        self.assertEqual(
            guest_client.get(SEARCH_FLAT_URL).status_code,
            200,
        )

    def test_template_for_url(self):
        """Проверка шаблона по адресу url"""
        guest_client = PropertyUrlTest.guest_client
        self.assertTemplateUsed(
            guest_client.get(HOMEPAGE),
            TEMPLATE_FILENAME,
        )
        self.assertTemplateUsed(
            guest_client.get(SEARCH_FLAT_URL),
            TEMPLATE_FILENAME,
        )
