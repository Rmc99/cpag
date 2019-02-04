from django.contrib import admin
from .models import Pagamento
from django.forms import TextInput
from django.db import models

class PagamentoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['pessoa']
    list_display = ('ano', 'mes', 'pessoa', 'categoria', 'funcao', 'valor_bruto', 'valor_liquido')
    search_fields = ['ano', 'mes', 'categoria', 'funcao', 'pessoa__nome']

    class Media:
        js = ('js/pessoa/jquery-3.3.1.min.js',)
        js = ('js/pagamento/jquery-calculo.js',)

    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
    }

admin.site.register(Pagamento, PagamentoAdmin)