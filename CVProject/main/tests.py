from django.test import TestCase
from django.urls import reverse
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