from django.db import models
from pessoa.models import Pessoa

class Pagamento(models.Model):
    SERVIDOR_CHOICE = (
        (True, "SIM"),
        (False, "NÃO"),
    )
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
    CATEGORIA_CHOICES = (
        (1, "Colaborador Interno"),
        (2, "Colaborador Externo"),
        (3, "Professor Interno"),
        (4, "Professor Externo"),
    )
    FUNCAO_CHOICES = (
        (1, "Administrativo"),
        (2, "Supervisor Orientador"),
        (3, "Coordenador"),
        (4, "Professor"),
    )
    ano = models.SmallIntegerField(null=False, verbose_name="Ano de Pagamento",help_text="Ex: 2019")
    mes = models.SmallIntegerField(null=False, choices=MES_CHOICES, verbose_name="Mês de Pagamento")
    pessoa = models.ForeignKey(Pessoa, related_name="pessoa", on_delete=models.CASCADE)
    categoria = models.SmallIntegerField(null=False, choices=CATEGORIA_CHOICES, verbose_name="Categoria")
    funcao = models.SmallIntegerField(null=False, choices=FUNCAO_CHOICES, verbose_name="Função")
    qtd_horas = models.SmallIntegerField(null=False, verbose_name="Quantidade de Horas no Mês")
    valor_hora = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Valor da Hora")
    valor_pensao = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Pensão Alimentícia")
    valor_bruto = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Valor Bruto", default=0)
    valor_inss = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Previdencia Oficial(INSS)", default=0, help_text="Taxa de 11%")
    valor_iss = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                              verbose_name="Valor Desconto ISS", default=0, help_text="Taxa de 5%")
    qtd_dependente_irpf = models.IntegerField(null=False, verbose_name="Dependentes (quantidade)", default=0, help_text="O valor da dedução é R$ 189,59 mensais, por dependente." )
    deducao_irpf = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                              verbose_name="Total de Deduções", default=0)
    valor_pos_deducao_irpf = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                              verbose_name="Valor Pós Dedução IRPF", default=0)
    valor_irpf = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                              verbose_name="IRPF", default=0)
    valor_liquido = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                              verbose_name="Valor Líquido", default=0)
    valor_patronal = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                              verbose_name="Patronal", default=0, help_text="Taxa de 20%")
    dta_criacao = models.DateTimeField(editable=False, auto_now_add=True)
    dta_atualizacao = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return str(self.ano)

    class Meta:
        verbose_name_plural = 'Pagamento'
        ordering = ['-ano', '-mes', '-categoria', '-funcao']
