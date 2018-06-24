from django.core import mail
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

    def test_inscricao_email_subject(self):
        expect = 'Confirmacao de Inscricao'
        self.assertEqual(expect, self.email.subject)

    def test_inscricao_email_from(self):
        expect = 'contato@eventex.com'
        self.assertEqual(expect, self.email.from_email)

    def test_inscricao_email_to(self):
        expect = ['contato@eventex.com', 'vicente.luz@armazemparaiba.com.br']
        self.assertEqual(expect, self.email.to)

    def test_inscricao_email_body(self):
        self.assertIn('Vicente Luz', self.email.body)
        self.assertIn('12345678901', self.email.body)
        self.assertIn('vicente.luz@armazemparaiba.com.br', self.email.body)
        self.assertIn('86-98822-1812', self.email.body)


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

