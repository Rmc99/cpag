from django.contrib import admin
from .models import Pagamento

class PagamentoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['pessoa']
    #list_display = ('ano','mes')
    #fields = ('ano', 'mes', 'pessoa')

admin.site.register(Pagamento, PagamentoAdmin)

