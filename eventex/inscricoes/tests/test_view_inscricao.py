from django.core import mail
from django.test import TestCase
from eventex.inscricoes.forms import InscricaoForm


class InscricaoGet(TestCase):
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
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))
        for tag, count in tags:
            with self.subTest():
                self.assertContains(self.resp, tag, count)

    def test_csrf(self):
        '''Html must contain csrf'''
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        '''Context must have inscricao Form'''
        form = self.resp.context['form']
        self.assertIsInstance(form, InscricaoForm)


class InscricaoPostValid(TestCase):
    def setUp(self):
        data = dict(name = 'Vicente Luz', cpf = '12345678901',
                    email = 'vicente.luz@armazemparaiba.com.br',
                    phone = '86-98822-1812')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]


    def test_post(self):
        '''Valid post redirect to /inscricao/'''
        self.assertEqual(302, self.resp.status_code)

    def test_send_inscricao_email(self):
        self.assertEqual(1, len(mail.outbox))


class InscricaoPostInvalid(TestCase):
    def setUp(self):
        data = dict()
        self.resp = self.client.post('/inscricao/', data)
        self.form = self.resp.context['form']

    def test_post(self):
        '''Invalid post should not redirect'''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'inscricao_form.html')

    def test_has_form(self):
        self.assertIsInstance(self.form, InscricaoForm)

    def test_form_has_errors(self):
        self.assertTrue(self.form.errors)

class InscricaoSuccessMessage(TestCase):
    def test_message(self):
        data = dict(name='Vicente Luz', cpf='12345678901',
                    email='vicente.luz@armazemparaiba.com.br',
                    phone='86-98822-1812')
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')

