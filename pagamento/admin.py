from django.contrib import admin
from .models import Pagamento, Categoria

class PagamentoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['pessoa']

admin.site.register(Pagamento, PagamentoAdmin)
admin.site.register(Categoria)


