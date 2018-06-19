from django.shortcuts import render

from eventex.inscricoes.forms import InscricaoForm


def inscricao(request):
    context = {'form': InscricaoForm()}
    return render(request, 'inscricao_form.html', context)