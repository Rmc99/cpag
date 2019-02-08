from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .models import Pagamento
from django.forms import TextInput
from django.db import models
from decimal import Decimal

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

    def response_change(self, request, obj):
        self.calcular(obj)
        obj.save()
        redirect_url = request.path
        messages.success(request, 'Pagamento Modificado com Sucesso!')
        return HttpResponseRedirect(redirect_url)
#        return redirect("/admin/pagamento/pagamento/")

    def response_add(self, request, obj):
        self.calcular(obj)
        obj.save()
        redirect_url = request.path
        messages.success(request, 'Pagamento Adicionado com Sucesso!')
        return HttpResponseRedirect(redirect_url)
#        return redirect("/admin/pagamento/pagamento/")

    def calcular(self, obj):
        tx_iss = Decimal(0.05)
        tx_patronal = Decimal(0.20)
        tx_por_dependente = Decimal(189.59)
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
        # calculo de 5% iss
        obj.valor_iss = (obj.valor_bruto * tx_iss)

        # tabela de calculo para inss
        if (obj.valor_bruto <= 1751.81):
            tx_inss = Decimal(0.08)
        elif (obj.valor_bruto >= 1751.82 and obj.valor_bruto <= 2919.72):
            tx_inss = Decimal(0.09)
        elif (obj.valor_bruto >= 2919.73 and obj.valor_bruto <= 5839.45):
            tx_inss = Decimal(0.11)

        if (obj.valor_bruto > 5839.46):
            obj.valor_inss = Decimal(642.34)
        else:
        # calculo de inss
            obj.valor_inss = (obj.valor_bruto * tx_inss)

        # calculo valor base para aplicar aliquota do irpf
        v_base = (obj.valor_bruto - obj.valor_inss)
        # calculo patronal
        obj.valor_patronal = (obj.valor_bruto * tx_patronal)
        # calculo deducao irpf
        obj.deducao_irpf = (obj.valor_inss + (obj.qtd_dependente_irpf * tx_por_dependente));
        # calculo pos deducao irpf
        obj.valor_pos_deducao_irpf = (obj.valor_bruto - obj.valor_inss - (obj.qtd_dependente_irpf * tx_por_dependente))

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
            #
            obj.valor_liquido = (obj.valor_bruto - obj.valor_inss - obj.valor_iss - obj.valor_irpf)
        # aliquota de 7,5%
        elif (v_base >= 1903.99 and v_base <= 2826.65):
            obj.valor_irpf = (obj.valor_bruto - (
                        obj.qtd_dependente_irpf * tx_por_dependente) - obj.valor_inss) * aliquota_1 - parc_deduzir_1
            obj.valor_liquido = (obj.valor_bruto - obj.valor_inss - obj.valor_iss - obj.valor_irpf)
        elif (v_base >= 2826.66 and v_base <= 3751.05):
            obj.valor_irpf = (obj.valor_bruto - (
                        obj.qtd_dependente_irpf * tx_por_dependente) - obj.valor_inss) * aliquota_2 - parc_deduzir_2
            obj.valor_liquido = (obj.valor_bruto - obj.valor_inss - obj.valor_iss - obj.valor_irpf)
        elif (v_base >= 3751.06 and v_base <= 4664.68):
            obj.valor_irpf = (obj.valor_bruto - (
                        obj.qtd_dependente_irpf * tx_por_dependente) - obj.valor_inss) * aliquota_3 - parc_deduzir_3
            obj.valor_liquido = (obj.valor_bruto - obj.valor_inss - obj.valor_iss - obj.valor_irpf)
        elif (v_base > 4664.68):
            obj.valor_irpf = (obj.valor_bruto - (
                        obj.qtd_dependente_irpf * tx_por_dependente) - obj.valor_inss) * aliquota_4 - parc_deduzir_4
            obj.valor_liquido = (obj.valor_bruto - obj.valor_inss - obj.valor_iss - obj.valor_irpf)

        return (obj)

    class Media:
        js = ('js/pagamento/jquery-3.3.1.min.js',)
        js = ('js/pagamento/jquery.mask.min.js',)

    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.DecimalField: {'widget': TextInput(attrs={'autocomplete': 'off'})},

    }
admin.site.register(Pagamento, PagamentoAdmin)
## todo reutilizar em ADD o metodo que faz os calculos em CHANGE