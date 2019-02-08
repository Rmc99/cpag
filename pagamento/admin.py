from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import Pagamento
from django.forms import TextInput
from django.db import models

class PagamentoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['pessoa']
    list_display = ('ano', 'mes', 'pessoa', 'categoria', 'funcao', 'valor_bruto', 'valor_irpf', 'valor_liquido')
    search_fields = ['ano', 'mes', 'categoria', 'funcao', 'pessoa__nome']
    fieldsets = (
        ('Dados do Pagamento:', {'fields': (('ano', 'mes', 'pessoa'), ('categoria', 'funcao', 'qtd_horas'),
         ('valor_hora', 'valor_pensao', 'qtd_dependente_irpf'))}),
        ('Calculos:', {'fields': (('valor_bruto', 'valor_inss',
             'valor_iss'), ('deducao_irpf', 'valor_pos_deducao_irpf', 'valor_irpf'), ('valor_liquido', 'valor_patronal'))}),
    )

    def response_change(self, request, obj):
        obj.ano = 4877
        obj.save()
        redirect_url = request.path
        return HttpResponseRedirect(redirect_url)


    class Media:
        js = ('js/pagamento/jquery-3.3.1.min.js',)
        js = ('js/pagamento/jquery.mask.min.js',)
#        js = ('js/pagamento/jquery-calculo.js',)
#        js = ('js/pagamento/jquery-mymask-pagamento.js',)


    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.DecimalField: {'widget': TextInput(attrs={'autocomplete': 'off'})},

    }

admin.site.register(Pagamento, PagamentoAdmin)