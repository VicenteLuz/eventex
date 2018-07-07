from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.inscricoes.forms import InscricaoForm
from eventex.inscricoes.models import Inscricao


def inscricao(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = InscricaoForm(request.POST)
    if not form.is_valid():
        return render(request, 'inscricao_form.html', {'form': form})


    envia_email('Confirmacao de Inscricao',
                settings.DEFAULT_FROM_EMAIL,
                form.cleaned_data['email'], 'inscricao_email.txt',
                form.cleaned_data)
    Inscricao.objects.create(**form.cleaned_data)
    messages.success(request, 'Inscrição realizada com sucesso!')

    return HttpResponseRedirect('/inscricao/')


def new(request):
    return render(request, 'inscricao_form.html', {'form': InscricaoForm()})


def envia_email(subject, de, para, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, de, [de, para])

