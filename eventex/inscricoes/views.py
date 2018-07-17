from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string
from eventex.inscricoes.forms import InscricaoForm
from eventex.inscricoes.models import Inscricao


def new(request):
    if request.method == 'POST':
        return create(request)

    return input_form(request)

def input_form(request):
    return render(request, 'inscricao_form.html', {'form': InscricaoForm()})


def create(request):
    form = InscricaoForm(request.POST)
    if not form.is_valid():
        return render(request, 'inscricao_form.html', {'form': form})

    incricao = Inscricao.objects.create(**form.cleaned_data)


    envia_email('Confirmacao de Inscricao',
                settings.DEFAULT_FROM_EMAIL,
                incricao.email,
                'inscricao_email.txt',
                {'inscricao': incricao})

    return HttpResponseRedirect(r('inscricoes:detail', incricao.pk))


def detail(request, pk):
    try:
        inscricao = Inscricao.objects.get(pk=pk)
    except Inscricao.DoesNotExist:
        raise Http404
    return render(request, 'inscricao_detail.html', {'inscricao': inscricao})


def envia_email(subject, de, para, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, de, [de, para])

