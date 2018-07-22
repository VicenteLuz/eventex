from unittest.mock import Mock

from django.test import TestCase
from eventex.inscricoes.admin import InscricaoModelAdmin, Inscricao, admin


class InscricaoModelAdminTest(TestCase):
    def setUp(self):
        Inscricao.objects.create(
            name='Vicente Luz',
            cpf='12345678901',
            email='vicente.luz@armazemparaiba.com.br',
            phone='86-98822-1812'
        )
        self.model_admin = InscricaoModelAdmin(Inscricao, admin.site)

    def test_has_action(self):
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        self.call_actions()
        self.assertEqual(1, Inscricao.objects.filter(paid=True).count())

    def test_message(self):
        mock = self.call_actions()
        mock.assert_called_once_with(None, '1 inscrição foi marcada como paga.')

    def call_actions(self):
        queryset = Inscricao.objects.all()

        mock = Mock()
        old_message_user = InscricaoModelAdmin.message_user
        InscricaoModelAdmin.message_user = mock

        self.model_admin.mark_as_paid(None, queryset)

        InscricaoModelAdmin.message_user = old_message_user

        return mock

