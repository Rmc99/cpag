from django.contrib import admin
from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'cpf')
    list_display = ('nome','email','cpf','pis','num_conta','num_agencia','num_operacao','num_banco')

    class Media:
        js = (
            'js/pessoa/jquery-3.3.1.min.js',
            'js/pessoa/jquery-mask.js',
        )
admin.site.register(Pessoa, PessoaAdmin)