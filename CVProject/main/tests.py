from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from .models import CV

class CVViewsTest(TestCase):
    def setUp(self):
        self.cv = CV.objects.create(
            firstname="John",
            lastname="Smith",
            bio="test CV",
            skills="Python, Django",
            projects="Project A, Project B",
            contacts="email: john@example.com"
        )

    def test_cv_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John")
        self.assertTemplateUsed(response, "home.html")

    def test_cv_detail_view(self):
        response = self.client.get(reverse('cv', args=[self.cv.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test CV")
        self.assertTemplateUsed(response, "detail.html")

    def test_cv_detail_404(self):
        response = self.client.get(reverse('cv', args=[999]))
        self.assertEqual(response.status_code, 404)


class CVAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.cv_data = {
            "firstname": "John",
            "lastname": "Doe",
            "skills": "Python, Django",
            "projects": "Blog, API",
            "bio": "Experienced dev",
            "contacts": "john@example.com"
        }
        self.cv = CV.objects.create(**self.cv_data)
        self.cv_url = reverse('cv-detail', kwargs={'pk': self.cv.pk})
        self.cv_list_url = reverse('cv-list')

    def test_create_cv(self):
        data = {
            "firstname": "Alice",
            "lastname": "Smith",
            "skills": "HTML, CSS",
            "projects": "Portfolio",
            "bio": "Frontend dev",
            "contacts": "alice@example.com"
        }
        response = self.client.post(self.cv_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CV.objects.count(), 2)

    def test_list_cvs(self):
        response = self.client.get(self.cv_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_cv(self):
        response = self.client.get(self.cv_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['firstname'], "John")

    def test_update_cv(self):
        update_data = self.cv_data.copy()
        update_data["skills"] = "Python, Django, REST"
        response = self.client.put(self.cv_url, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("REST", response.data["skills"])

    def test_delete_cv(self):
        response = self.client.delete(self.cv_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CV.objects.count(), 0)

