from django import forms
from django.core.exceptions import ValidationError


def valida_cpf(value):
    if not value.isdigit():
        raise ValidationError('cpf deve conter apenas numeros, verifique!', 'digito')

    if len(value) != 11:
        raise ValidationError('cpf deve conter 11 digitos, verifique!','tamanho')

class InscricaoForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[valida_cpf])
    email = forms.EmailField(label='E-mail')
    phone = forms.CharField(label='Fone')
