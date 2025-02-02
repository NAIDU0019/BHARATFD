from rest_framework.test import APITestCase
from django.urls import reverse
from faq_app.models import FAQ  # Ensure model is imported

class FAQAPITests(APITestCase):
    def test_get_faq_list(self):
        url = reverse('faq-list')  # Ensure the URL name matches urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_faq_with_lang(self):
        url = reverse('faq-list') + '?lang=es'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_pagination(self):
        url = reverse('faq-list') + '?page=1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_filtering(self):
        url = reverse('faq-list') + '?filter=test'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_sorting(self):
        url = reverse('faq-list') + '?sort=question'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
