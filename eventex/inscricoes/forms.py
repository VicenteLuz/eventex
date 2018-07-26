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
    email = forms.EmailField(label='E-mail', required=False)
    phone = forms.CharField(label='Fone', required=False)

    def clean_name(self):
        name = self.cleaned_data['name']
        #words = []
        #for w in name.split():
            #words.append(w.capitalize())
        words = [w.capitalize() for w in name.split() ]
        return ' '.join(words)

    def clean(self):
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu E-mail ou Telefone')
        return self.cleaned_data
