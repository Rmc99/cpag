from django.db import models
from pessoa.models import Pessoa

class Categoria(models.Model):
    nome = models.CharField(max_length=50, null=False, verbose_name="Categoria", blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Categoria'

class Pagamento(models.Model):
    MES_CHOICES = (
        (1, "Janeiro"),
        (2, "Fevereiro"),
        (3, "Março"),
        (4, "Abril"),
        (5, "Maio"),
        (6, "Junho"),
        (7, "Julho"),
        (8, "Agosto"),
        (9, "Setembro"),
        (10, "Outubro"),
        (11, "Novembro"),
        (12, "Dezembro"),
    )
    FUNCAO_CHOICES = (
        (1, "Administrativo"),
        (2, "Supervisor Orientador"),
        (3, "Coordenador"),
    )
    ano = models.IntegerField(null=False, verbose_name="Ano de Pagamento", blank=True, help_text="Ex: 2019")
    mes = models.IntegerField(null=False, choices=MES_CHOICES, verbose_name="Mês de Pagamento", blank=True)
    pessoa = models.ForeignKey(Pessoa, related_name="pessoa", on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, related_name="categoria", on_delete=models.CASCADE)
    funcao = models.IntegerField(null=False, choices=FUNCAO_CHOICES, verbose_name="Função", blank=True)
    qtd_horas = models.IntegerField(null=False, verbose_name="Quantidade de Horas no Mês", blank=True)
    valor_hora = models.DecimalField(max_digits=7, decimal_places=2, null=False, verbose_name="Valor da Hora")
    valor_bruto = models.DecimalField(max_digits=7, decimal_places=2, null=False, verbose_name="Valor Bruto")
    valor_base_desc_inss = models.DecimalField(max_digits=7, decimal_places=2, null=False, verbose_name="Valor Base Desconto INSS")
    valor_base_desc_iss = models.DecimalField(max_digits=7, decimal_places=2, null=False,
                                              verbose_name="Valor Base Desconto ISS")
    qtd_dependente_irpf = models.IntegerField(null=False, verbose_name="Quantidade de Dependentes de IRPF", blank=True)
    valor_deducao_irpf = models.DecimalField(max_digits=7, decimal_places=2, null=False,
                                              verbose_name="Valor Dedução IRPF")
    valor_pos_deducao_irpf = models.DecimalField(max_digits=7, decimal_places=2, null=False,
                                              verbose_name="Valor Pós Dedução IRPF")
    valor_irpf = models.DecimalField(max_digits=7, decimal_places=2, null=False,
                                              verbose_name="IRPF")
    valor_liquido = models.DecimalField(max_digits=7, decimal_places=2, null=False,
                                              verbose_name="Valor Líquido")
    valor_patronal = models.DecimalField(max_digits=7, decimal_places=2, null=False,
                                              verbose_name="Patronal")
    dta_criacao = models.DateTimeField(editable=False, auto_now_add=True)
    dta_atualizacao = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return self.ano

    class Meta:
        verbose_name_plural = 'Pagamento'
