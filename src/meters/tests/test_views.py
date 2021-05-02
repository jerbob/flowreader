"""Test views associated with the 'meters' app."""

from django.test import TestCase


class RedirectsTestCase(TestCase):
    """Test RedirectViews in the project."""

    def test_index_admin_redirect(self) -> None:
        """Test that requests to '/' redirect to the admin site."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/admin")
