from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from clientes.models import Endereco

# Create your models here.
class Perfil(models.Model):
    #FEMININO, MASCULINO
    SEXO = (
        ('F', 'FEMININO'),
        ('M', 'MASCULINO'),
    )

    VENDEDOR = 1
    CAIXA = 2
    ADMIN = 3

    #VENDEDOR, CAIXA, SUPERVISOR, ADMINISTRADOR
    TIPOS_USUARIOS = (
        (VENDEDOR, 'VENDEDOR'),
        (CAIXA, 'CAIXA'),
        (ADMIN, 'ADMINISTRADOR'),
    )

    #CASADO, DIVORCIADO, SOLTEIRO, VIUVO
    ESTADO_CIVIL = (
        (1, 'CASADO(A)'),
        (2, 'DIVORCIADO(A)'),
        (3, 'SEPARADO(A)'),
        (4, 'SOLTEIRO(A)'),
        (5, 'VIUVO(A)'),
    )

    usuario      = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE, default=True)
    tipo_usuario = models.PositiveSmallIntegerField(_('Tipo de Usuário'), choices=TIPOS_USUARIOS, default=VENDEDOR)
    sexo         = models.CharField(max_length=1, choices=SEXO)
    fone         = models.CharField(_('Telefone'), max_length=11, blank=True, null=True)
    cpf          = models.CharField(unique=True, max_length=11)
    data_nasc    = models.DateField(_('Data de Nascimento'), blank=True, null=True)
    estado_civil = models.PositiveSmallIntegerField(_('Estado Civil'), choices=ESTADO_CIVIL, null=True, blank=True)
    obs          = models.TextField(null=True, blank=True)
    #endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True, blank=True)

