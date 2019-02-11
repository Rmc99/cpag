from django.contrib import admin
from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'cpf')
    #list_display = ('nome', 'email', 'cpf', 'pis', 'num_conta', 'num_agencia', 'num_operacao', 'num_banco')
    #fields = ('nome', 'email', 'cpf', 'pis', 'num_conta', 'num_agencia', 'num_operacao', 'num_banco')
    fieldsets = (
        ('Dados Pessoais:', {'fields': (('nome', 'email'), ('telefone', 'cpf'), 'pis')}),
        ('Dados Bancários:', {'fields': (('num_conta', 'num_agencia'), ('num_operacao', 'num_banco'))}),
    )
    class Media:
        js = (
            'js/pessoa/jquery-3.3.1.min.js',
            'js/pessoa/jquery.mask.min.js',
            'js/pessoa/jquery-mymask.js',
        )
admin.site.register(Pessoa, PessoaAdmin)