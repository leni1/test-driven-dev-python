from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase

from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolve_home_page_view(self):
        url = resolve('/')
        self.assertEqual(url.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        resp = home_page(request)
        html = resp.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
