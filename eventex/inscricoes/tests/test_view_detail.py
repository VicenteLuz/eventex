from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.inscricoes.models import Inscricao


class InscricaoDetailGet(TestCase):
    def setUp(self):
        self.obj = Inscricao.objects.create(
            name = 'Vicente Luz',
            cpf = '12345678901',
            email = 'vicente@frigotil.com.br',
            phone = '86-98822-1812')
        self.resp = self.client.get(r('inscricoes:detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'inscricao_detail.html')

    def test_context(self):
        inscricao = self.resp.context['inscricao']
        self.assertIsInstance(inscricao, Inscricao)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)

        with self.subTest():
            for content in contents:
                self.assertContains(self.resp, content)

class InscricaoDetailNotFound(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('inscricoes:detail', 0))

    def test_not_found(self):
        self.assertEqual(404, self.resp.status_code)
