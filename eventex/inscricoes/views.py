from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.inscricoes.forms import InscricaoForm


def inscricao(request):
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            context = dict(name = 'Vicente Luz', cpf = '12345678901',
                           email = 'vicente.luz@armazemparaiba.com.br',
                           phone = '86-98822-1812')
            body = render_to_string('inscricao_email.txt', form.cleaned_data)
            mail.send_mail('Confirmacao de Inscricao',
                            body,
                            'contato@eventex.com',
                           ['contato@eventex.com', form.cleaned_data['email']])
            messages.success(request, 'Inscrição realizada com sucesso!')

            return HttpResponseRedirect('/inscricao/')
        else:
            return render(request, 'inscricao_form.html', {'form':form})
    else:
        context = {'form': InscricaoForm()}
        return render(request, 'inscricao_form.html', context)

