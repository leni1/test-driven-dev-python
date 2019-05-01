from django.urls import resolve
from django.test import TestCase

from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolve_home_page_view(self):
        url = resolve('/')
        self.assertEqual(url.func, home_page)
