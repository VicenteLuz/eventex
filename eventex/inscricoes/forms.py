from django import forms
from django.core.exceptions import ValidationError

from eventex.inscricoes.models import Inscricao
from eventex.inscricoes.validators import valida_cpf


class InscricaoFormOld(forms.Form):
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


class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['name', 'cpf', 'email', 'phone']

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

