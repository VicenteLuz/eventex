from django.test import TestCase

from eventex.inscricoes.forms import InscricaoForm


class inscricaoFormTest(TestCase):
    def test_has_fields(self):
        '''Form must have foour fields'''
        form = InscricaoForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_isdigit(self):
        form = self.make_valida_form(cpf='ABCD5678901')
        #self.assertFormErrorMessage(form, 'cpf', 'cpf deve conter apenas numeros, verifique!')
        self.assertErrorCode(form, 'cpf', 'digito')

    def test_cpf_contem_11_digitos(self):
        form = self.make_valida_form(cpf='12345')
        #self.assertFormErrorMessage(form, 'cpf', 'cpf deve conter 11 digitos, verifique!')
        self.assertErrorCode(form, 'cpf', 'tamanho')

    def test_capitalize_name(self):
        form = self.make_valida_form(name='VICENTE oliveira LUZ')
        self.assertEqual('Vicente Oliveira Luz', form.cleaned_data['name'])

    def test_email_optional(self):
        form = self.make_valida_form(email='')
        self.assertFalse(form.errors)

    def test_phone_optional(self):
        form = self.make_valida_form(phone='')
        self.assertFalse(form.errors)

    def test_informe_email_or_phone(self):
        form = self.make_valida_form(email='', phone='')
        self.assertListEqual(list(['__all__']), list(form.errors))

    def assertErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_valida_form(self, **kwargs):
        valid = dict(
            name='Vicente Luz',
            cpf='12345678901',
            email='vicente.luz@armazemparaiba.com.br',
            phone='86-98822-1812'
        )
        data = dict(valid, **kwargs)
        form = InscricaoForm(data)
        form.is_valid()
        return form
