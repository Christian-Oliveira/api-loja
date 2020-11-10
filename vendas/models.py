from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from clientes.models import Cliente
from produtos.models import Produto

# Create your models here.
class Base(models.Model):
    criado_em     = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo         = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Venda(Base):
    DINHEIRO = 1
    CREDITO  = 2
    DEBITO   = 3
    CARNE    = 4

    FORMA_PAGAMENTO = (
        (DINHEIRO, "Dinheiro"),
        (CREDITO, "Credito"),
        (DEBITO, "Debito"),
        (CARNE, "Carnê")
    )

    STATUS = (
        ("P", "PENDENTE"),
        ("F", "FINALIZADO"),
    )

    cliente         = models.ForeignKey(Cliente, related_name="compras", on_delete=models.PROTECT)
    vendedor        = models.ForeignKey(User, related_name="vendas", on_delete=models.PROTECT)
    produtos        = models.ManyToManyField(Produto, through='ItemVenda')
    valor_total     = models.DecimalField(_("Valor Total"), max_digits=10, decimal_places=2, null=True, blank=True)
    desconto        = models.PositiveIntegerField(_("Desconto"), null=True, blank=True)
    forma_pagamento = models.PositiveIntegerField(_("Forma de Pagamento"), choices=FORMA_PAGAMENTO, null=True, blank=True)
    valor_pago      = models.DecimalField(_("Valor Pago"), max_digits=10, decimal_places=2, null=True, blank=True)
    qtd_parcelas    = models.PositiveIntegerField(_("Quantidade de Parcelas"), null=True, blank=True)
    valor_parcelas  = models.DecimalField(_("Valor das Parcelas"), max_digits=10, decimal_places=2, null=True, blank=True)
    venc_parcelas   = models.DateField(_("Vencimento das Parcelas"), null=True, blank=True)
    status          = models.CharField(_("Status"), choices=STATUS, max_length=1)

    
class ItemVenda(models.Model):
    produto        = models.ForeignKey(Produto, on_delete=models.PROTECT)
    venda          = models.ForeignKey(Venda, on_delete=models.CASCADE)
    quantidade     = models.PositiveIntegerField(_("Quantidade"))
    preco_unitario = models.DecimalField(_("Preço Unitário"), max_digits=10, decimal_places=2)
    preco_total    = models.DecimalField(_("Preço Total"), max_digits=10, decimal_places=2)


class Parcelas(models.Model):
    STATUS = (
        ("A", "ABERTO"),
        ("V", "VENCIDO"),
        ("P", "PAGO"),
    )


    num_parcelas   = models.PositiveSmallIntegerField(_("Número de Parcelas"))
    valor_parcela  = models.DecimalField(_("Valor da Parcela"), max_digits=10, decimal_places=2)
    venc_parcela   = models.DateField()
    status         = models.CharField(_("Status"), max_length=1, choices=STATUS, default="A")
    data_pagamento = models.DateField(null=True, blank=True)
    juros          = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_pago     = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    id_venda       = models.ForeignKey(Venda, related_name="parcelas", on_delete=models.CASCADE)

