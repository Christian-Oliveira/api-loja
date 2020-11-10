from django.db import models
from django.utils.translation import ugettext_lazy as _

from clientes.models import Endereco

# Create your models here.
class Base(models.Model):
    criado_em     = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo         = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Categoria(Base):
    nome = models.CharField(max_length=150, unique=True)

    def clean(self):
        self.nome = self.nome.upper()
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Marca(Base):
    nome = models.CharField(max_length=150, unique=True)

    def clean(self):
        self.nome = self.nome.upper()
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Produto(Base):
    #FEMININO, MASCULINO
    GENERO = (
        ("F", "FEMININO"),
        ("M","MASCULINO")
    )

    #ADULTO, TEENS, KIDS, BABY
    TIPO = (
        ("A", "ADULTO"),
        ("T", "TEENS"),
        ("K", "KIDS"),
        ("B", "BABY")
    )

    codigo      = models.CharField(_("Código"), max_length=8, editable=False, unique=True, null=True)
    categoria   = models.ForeignKey(Categoria, related_name='categoria_produtos', on_delete=models.PROTECT)
    marca       = models.ForeignKey(Marca, related_name='marca_produtos', on_delete=models.PROTECT)
    descricao   = models.CharField(_("Descrição"), max_length=150)
    estoque     = models.PositiveIntegerField(_("Estoque"))
    estoque_min = models.PositiveIntegerField(_("Estoque Mínimo"), default=1)
    preco       = models.DecimalField(_("Preço"), max_digits=10, decimal_places=2) #99.999.99,99
    genero      = models.CharField(_("Gênero"), max_length=1, choices=GENERO)
    tipo        = models.CharField(_("Tipo"), max_length=1, choices=TIPO, null=True, blank=True)
    tamanho     = models.CharField(_("Tamanho"), max_length=3)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        
    def __str__(self):
        return self.descricao


    