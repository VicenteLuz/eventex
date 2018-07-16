from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class InscricaoPostValid(TestCase):
    def setUp(self):
        data = dict(name = 'Vicente Luz', cpf = '12345678901',
                    email = 'vicente.luz@armazemparaiba.com.br',
                    phone = '86-98822-1812')
        self.client.post(r('inscricoes:new'), data)
        self.email = mail.outbox[0]

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
        contents = [
            'Vicente Luz', '12345678901',
            'vicente.luz@armazemparaiba.com.br', '86-98822-1812'
        ]
        for content in contents:
            self.assertIn(content, self.email.body)
        