from django.db import models

class Pessoa(models.Model):
    BANCO_CHOICES = (
        ("001", "001-Banco do Brasil S.A."),
        ("341", "341-Banco Itaú S.A."),
        ("033", "033-Banco Santander (Brasil) S.A."),
        ("356", "356-Banco Real S.A. (antigo)"),
        ("652", "652-Itaú Unibanco Holding S.A."),
        ("237", "237-Banco Bradesco S.A."),
        ("745", "745-Banco Citibank S.A."),
        ("399", "399-HSBC Bank Brasil S.A. – Banco Múltiplo"),
        ("104", "104-Caixa Econômica Federal"),
        ("389", "389-Banco Mercantil do Brasil S.A."),
        ("453", "453-Banco Rural S.A."),
        ("422", "422-Banco Safra S.A."),
        ("633", "633-Banco Rendimento S.A."),
    )
    nome = models.CharField(max_length=150, null=False, verbose_name="Nome Completo", blank=True)
    email = models.EmailField(max_length=150, null=True, verbose_name="E-Mail", blank=True)
    telefone = models.CharField(max_length=16, null=True, verbose_name="Telefone", blank=True, help_text="Ex: 00-00000-0000")
    cpf = models.CharField(max_length=14, null=False, verbose_name="CPF", blank=True)
    pis = models.CharField(max_length=25, null=False, verbose_name="PIS", blank=True)
    num_conta = models.CharField(max_length=30, null=False, verbose_name="Conta", blank=True)
    num_agencia = models.CharField(max_length=30, null=False, verbose_name="Agência", blank=True)
    num_operacao = models.CharField(max_length=30, null=False, verbose_name="Operação", blank=True)
    num_banco = models.CharField(max_length=10, null=False, choices=BANCO_CHOICES, verbose_name="Número do Banco", blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Pessoa'
