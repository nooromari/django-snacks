from django.conf.urls import url
from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class snacks_tasts (SimpleTestCase):
    def test_home_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_tampletes(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'home.html')

    def test_about_status(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_tampletes(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'about.html')