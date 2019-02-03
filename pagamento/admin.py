from django.contrib import admin
from .models import Pagamento

class PagamentoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['pessoa']
    list_display = ('ano', 'mes', 'pessoa', 'categoria', 'funcao', 'valor_bruto', 'valor_liquido')
    search_fields = ['ano', 'mes', 'categoria', 'funcao', 'pessoa__nome']

admin.site.register(Pagamento, PagamentoAdmin)

