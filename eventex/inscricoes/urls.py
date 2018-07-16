from django.urls import path, register_converter

from eventex.inscricoes.views import new, detail
from eventex.lib.urlconverter import MaskConverter

register_converter(MaskConverter, 'mask')
app_name = 'inscricoes'
urlpatterns = [
    path('', new, name='new'),
    path('<int:pk>/', detail, name='detail'),
    #path('inscricao/<mask:pk>/', detail, name='detail'),
]
