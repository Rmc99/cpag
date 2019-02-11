from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .models import Pagamento
from django.forms import TextInput
from django.db import models
from decimal import Decimal, InvalidOperation


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
    list_filter = ('ano', 'mes', 'categoria', 'funcao', 'pessoa__nome')

    def response_change(self, request, obj):
        self.calcular(obj)
        try:
            obj.save()
            redirect_url = request.path
            messages.success(request, 'Pagamento Modificado com Sucesso!')
            return HttpResponseRedirect(redirect_url)
        except InvalidOperation:
            redirect_url = request.path
            messages.error(request, 'ERRO! Verifique se os dados inseridos estão corretos!')
            return HttpResponseRedirect(redirect_url)

#        return redirect("/admin/pagamento/pagamento/")

    def response_add(self, request, obj):
        self.calcular(obj)
        try:
            obj.save()
            messages.success(request, 'Pagamento Adicionado com Sucesso!')
            redirect_url = request.path
            return HttpResponseRedirect(redirect_url)
        except InvalidOperation:
            redirect_url = request.path
            messages.error(request, 'ERRO! Verifique se os dados inseridos estão corretos!')
            return HttpResponseRedirect(redirect_url)

    def calcular(self, obj):
        tx_iss = Decimal(0.05)
        tx_patronal = Decimal(0.20)
        tx_por_dependente = Decimal(189.59)
        tx_inss = Decimal(0.11)
        aliquota_1 = Decimal(0.075)
        parc_deduzir_1 = Decimal(142.80)
        aliquota_2 = Decimal(0.15)
        parc_deduzir_2 = Decimal(354.80)
        aliquota_3 = Decimal(0.225)
        parc_deduzir_3 = Decimal(636.13)
        aliquota_4 = Decimal(0.275)
        parc_deduzir_4 = Decimal(869.36)

        # calculo do valor bruto
        obj.valor_bruto = (obj.qtd_horas * obj.valor_hora)
        # calculo de inss
        obj.valor_inss = (obj.valor_bruto * tx_inss)
        # calculo de 5% iss
        obj.valor_iss = (obj.valor_bruto * tx_iss)

        # calculo valor base para aplicar aliquota do irpf
        v_base = (obj.valor_bruto - obj.valor_inss)
        # calculo patronal
        obj.valor_patronal = (obj.valor_bruto * tx_patronal)
        # calculo deducao irpf
        obj.deducao_irpf = (obj.valor_inss + obj.valor_pensao + (obj.qtd_dependente_irpf * tx_por_dependente));
        # calculo pos deducao irpf
        obj.valor_pos_deducao_irpf = (obj.valor_bruto - obj.valor_inss - obj.valor_pensao - (obj.qtd_dependente_irpf * tx_por_dependente))

        # calculos para colaborador/professor interno do ifma/colun
        if (obj.categoria == 1 or obj.categoria == 3):
            obj.valor_liquido = obj.valor_bruto
            obj.valor_inss = 0
            obj.valor_iss = 0
            obj.deducao_irpf = 0
            obj.valor_irpf = 0
            obj.valor_pos_deducao_irpf = 0
            obj.valor_patronal = 0
        # isento de irpf
        elif (v_base <= 1903.98):
            obj.valor_irpf = 0
            # inclui mas consultar jorge
            obj.deducao_irpf = 0
            obj.valor_irpf = 0
            obj.valor_pos_deducao_irpf = 0
            obj.valor_liquido = (obj.valor_bruto - obj.valor_inss - obj.valor_iss - obj.valor_irpf)
        # aliquota de 7,5%
        elif (v_base >= 1903.99 and v_base <= 2826.65):
            obj.valor_irpf = (obj.valor_bruto - (
                        obj.qtd_dependente_irpf * tx_por_dependente) - obj.valor_inss - obj.valor_pensao) * aliquota_1 - parc_deduzir_1
            if (obj.valor_irpf <=0):
                obj.valor_irpf = 0
            obj.valor_liquido = (obj.valor_bruto - obj.valor_inss - obj.valor_iss - obj.valor_irpf)
        elif (v_base >= 2826.66 and v_base <= 3751.05):
            obj.valor_irpf = (obj.valor_bruto - (
                        obj.qtd_dependente_irpf * tx_por_dependente) - obj.valor_inss - obj.valor_pensao) * aliquota_2 - parc_deduzir_2
            if (obj.valor_irpf <=0):
                obj.valor_irpf = 0
            obj.valor_liquido = (obj.valor_bruto - obj.valor_inss - obj.valor_iss - obj.valor_irpf)
        elif (v_base >= 3751.06 and v_base <= 4664.68):
            obj.valor_irpf = (obj.valor_bruto - (
                        obj.qtd_dependente_irpf * tx_por_dependente) - obj.valor_inss - obj.valor_pensao) * aliquota_3 - parc_deduzir_3
            if (obj.valor_irpf <=0):
                obj.valor_irpf = 0
            obj.valor_liquido = (obj.valor_bruto - obj.valor_inss - obj.valor_iss - obj.valor_irpf)
        elif (v_base > 4664.68):
            obj.valor_irpf = (obj.valor_bruto - (
                        obj.qtd_dependente_irpf * tx_por_dependente) - obj.valor_inss - obj.valor_pensao) * aliquota_4 - parc_deduzir_4
            if (obj.valor_irpf <=0):
                obj.valor_irpf = 0
            obj.valor_liquido = (obj.valor_bruto - obj.valor_inss - obj.valor_iss - obj.valor_irpf)
        return (obj)

    class Media:
        js = (
            'js/pagamento/jquery-3.3.1.min.js',
            'js/pagamento/jquery.mask.min.js',
            'js/pagamento/jquery-mymask-pagamento.js',
        )

    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.DecimalField: {'widget': TextInput(attrs={'autocomplete': 'off'})},

    }
admin.site.register(Pagamento, PagamentoAdmin)
## todo alterar nome de botões no admin e exportar arquivos para csv
