from django.test import TestCase, Client
from django.urls import reverse


class IndexPageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        """Test that the index page renders ok"""
        url = reverse('doctor:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
