from django.contrib import admin
from django.utils.timezone import now
from eventex.inscricoes.models import Inscricao


class InscricaoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone', 'created_at',
                    'inscrito_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'cpf', 'phone', 'created_at', 'paid')
    list_filter = ('paid', 'created_at')

    actions = ['mark_as_paid']

    def inscrito_today(self, obj):
        return obj.created_at == now().date()

    inscrito_today.short_description = 'inscrito hoje?'
    inscrito_today.boolean =True

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)
        if count == 1:
            msg = '{} inscrição foi marcada como paga.'
        else:
            msg = '{} inscrições foram marcadas como pagas.'

        self.message_user(request, msg.format(count))

    mark_as_paid.short_description = "Marcar como pago"

admin.site.register(Inscricao, InscricaoModelAdmin)