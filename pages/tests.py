# pages/tests.py
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import LandingPageView


class LandingPageTests(SimpleTestCase):
    ##TODO: create setUp function to replace repeated response = self.client request
    ## note on above: url = reverse("landing"); self.response = self.client.get(url) within setUp()
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_landingpage_url_name(self):
        response = self.client.get(reverse("landing"))
        self.assertEqual(response.status_code, 200)

    def test_landingpage_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "landing.html")

    def test_landingpage_contains_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "Card1")

    def test_landingpage_does_not_contain_incorrect_html(self):
        response = self.client.get("/")
        # place holder test, in future replace str with text from a different page's html
        self.assertNotContains(response, "text from some other html file")

    def test_landingpage_url_resolves_landingpageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, LandingPageView.as_view().__name__)
