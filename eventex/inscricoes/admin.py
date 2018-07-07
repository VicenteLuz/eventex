from django.contrib import admin
from django.utils.timezone import now

from eventex.inscricoes.models import Inscricao


class InscricaoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone', 'created_at', 'inscrito_today')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'cpf', 'phone', 'created_at')
    list_filter = ('created_at',)

    def inscrito_today(self, obj):
        return obj.created_at == now().date()
    inscrito_today.short_description = 'inscrito hoje?'
    inscrito_today.boolean =True

admin.site.register(Inscricao, InscricaoModelAdmin)