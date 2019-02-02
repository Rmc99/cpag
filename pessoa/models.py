from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=150, null=False, verbose_name="Nome Completo", blank=True)
    email = models.EmailField(max_length=150, null=True, verbose_name="E-Mail", blank=True)
    cpf = models.CharField(max_length=14, null=False, verbose_name="CPF", blank=True)
    pis = models.CharField(max_length=25, null=False, verbose_name="PIS", blank=True)
    num_conta = models.IntegerField(null=False, verbose_name="Conta", blank=True)
    num_agencia = models.IntegerField(null=False, verbose_name="Agência", blank=True)
    num_operacao = models.IntegerField(null=False, verbose_name="Operação", blank=True)
    num_banco = models.IntegerField(null=False, verbose_name="Número do Banco", blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Pessoa'
