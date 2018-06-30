from django.test import TestCase

from eventex.inscricoes.forms import InscricaoForm


class inscricaoFormTest(TestCase):
    def setUp(self):
        self.form = InscricaoForm()

    def test_has_fields(self):
        '''Form must have foour fields'''
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))


