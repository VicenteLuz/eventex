from django.test import TestCase
from eventex.inscricoes.forms import InscricaoForm


class InscricaoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        '''Get /inscricao/ must return status code 200'''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        '''Must use /inscricao/incricao_form.html'''
        self.assertTemplateUsed(self.resp, 'inscricao_form.html')

    def test_html(self):
        '''Html must contain input tags'''
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        '''Html must contain csrf'''
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        '''Context must have inscricao Form'''
        form = self.resp.context['form']
        self.assertIsInstance(form, InscricaoForm)

    def test_has_fields(self):
        '''Form must have foour fields'''
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))