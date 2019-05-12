from django.test import TestCase


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        resp = self.client.get('/')
        self.assertTemplateUsed(resp, 'home.html')

    def test_can_save_post_request(self):
        resp = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', resp.content.decode())
        self.assertTemplateUsed(resp, 'home.html')
