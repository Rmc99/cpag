from django.contrib import admin
from .models import Pagamento
from django.forms import TextInput
from django.db import models

class PagamentoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['pessoa']
    list_display = ('ano', 'mes', 'pessoa', 'categoria', 'funcao', 'valor_bruto', 'valor_liquido')
    search_fields = ['ano', 'mes', 'categoria', 'funcao', 'pessoa__nome']
    fields = ['ano', 'mes', 'pessoa', 'categoria', 'funcao', 'qtd_horas',
              'valor_hora', 'valor_pensao', 'status_servidor', 'qtd_dependente_irpf', 'valor_bruto', 'valor_base_desc_inss',
              'valor_base_desc_iss', 'valor_deducao_irpf',
              'valor_pos_deducao_irpf', 'valor_irpf', 'valor_liquido', 'valor_patronal']

    class Media:
        js = ('js/pagamento/jquery-3.3.1.min.js',)
        js = ('js/pagamento/jquery.mask.min.js',)
        js = ('js/pagamento/jquery-calculo.js',)
        js = ('js/pagamento/jquery-mymask-pagamento.js',)

    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.DecimalField: {'widget': TextInput(attrs={'autocomplete': 'off'})},

    }

admin.site.register(Pagamento, PagamentoAdmin)