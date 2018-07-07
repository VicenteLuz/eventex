from datetime import datetime

from django.test import TestCase
from eventex.inscricoes.models import Inscricao


class inscricaoModelTest(TestCase):
    def setUp(self):
        self.obj = Inscricao(
            name = 'Vicente Luz',
            cpf = '12345678901',
            email = 'vicente.luz@armazemparaiba.com.br',
            phone = '86-98822-1812'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Inscricao.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Vicente Luz', str(self.obj))