from django.contrib import admin
from .models import Pessoa


class PessoaAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'cpf')
    list_display = ('nome','email','cpf','pis','num_conta','num_agencia','num_operacao','num_banco')


admin.site.register(Pessoa, PessoaAdmin)