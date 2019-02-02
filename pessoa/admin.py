from django.contrib import admin
from .models import Pessoa


class PessoaAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'cpf')

admin.site.register(Pessoa, PessoaAdmin)