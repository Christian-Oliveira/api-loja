from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Base(models.Model):
    criado_em     = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo         = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Endereco(Base):
    logradouro  = models.CharField(max_length=255)
    bairro      = models.CharField(max_length=100)
    cep         = models.CharField(max_length=8)
    numero      = models.PositiveSmallIntegerField(blank=True, null=True)
    uf          = models.CharField(max_length=2)
    cidade      = models.CharField(max_length=100)
    ponto_ref   = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
    
    def __str__(self):
        return self.logradouro


class Cliente(Base):
    #FEMININO, MASCULINO
    SEXO = (
        ('F', 'FEMININO'),
        ('M', 'MASCULINO'),
    )

    #CASADO, DIVORCIADO, SOLTEIRO, VIUVO
    ESTADO_CIVIL = (
        (1, 'CASADO(A)'),
        (2, 'DIVORCIADO(A)'),
        (3, 'SEPARADO(A)'),
        (4, 'SOLTEIRO(A)'),
        (5, 'VIUVO(A)'),
    )

    #ATIVO, SPC, SUSPENSO, FICHA IMPRESSA
    STATUS = (
        (1, 'ATIVO'),
        (2, 'SPC'),
        (3, 'SUSPENSO'),
    )

    nome           = models.CharField(max_length=100)
    cpf            = models.CharField(max_length=11, unique=True)
    rg             = models.CharField(max_length=15, blank=True, null=True)
    sexo           = models.CharField(max_length=1, choices=SEXO)
    data_nasc      = models.DateField()
    fone           = models.CharField(max_length=11)
    fone_recado    = models.CharField(max_length=11, null=True, blank=True)
    email          = models.EmailField(null=True, blank=True)
    estado_civil   = models.PositiveSmallIntegerField(choices=ESTADO_CIVIL)
    conjuge        = models.CharField(max_length=100, blank=True, null=True)
    apelido        = models.CharField(max_length=50, blank=True, null=True)
    filiacao       = models.CharField(max_length=100, null=True, blank=True)
    status         = models.PositiveSmallIntegerField(choices=STATUS, default=1)
    credito        = models.DecimalField(max_digits=8, decimal_places=2)
    obs            = models.TextField(blank=True, null=True)
    criado_por     = models.ForeignKey(User, related_name='clientes', on_delete=models.PROTECT)
    endereco       = models.ForeignKey(Endereco, related_name="enderecos", on_delete=models.SET_NULL, null=True)
    end_entrega    = models.ForeignKey(Endereco, related_name="enderecos_entregas", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nome']
        
    def __str__(self):
        return self.nome