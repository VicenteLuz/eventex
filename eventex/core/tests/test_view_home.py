from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('home'))

    def test_get(self):
        '''Get / Must status code 200 '''
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        '''Must use index.html'''
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_inscricao_link(self):
        expected = 'href="{}"'.format(r('inscricoes:new'))
        self.assertContains(self.resp, expected)
