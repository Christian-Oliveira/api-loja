from rest_framework import serializers
from faker import Faker

from .models import Categoria, Marca, Produto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']
        read_only_fields = ['id']


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nome']
        read_only_fields = ['id']


class ProdutoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = [
            'codigo',
            'categoria',
            'marca',
            'descricao',
            'estoque',
            'estoque_min',
            'preco',
            'genero',
            'tipo',
            'tamanho'
        ]

        read_only_fields = ['codigo']

    def create(self, validated_data):
        fake = Faker()
        validated_data['codigo'] = None
        while (validated_data['codigo'] is None):
            codigo = fake.ean(length=8)
            produtoIsExists = Produto.objects.filter(codigo=codigo)
            if not(produtoIsExists.exists()):
                validated_data['codigo'] = codigo

        produto = Produto.objects.create(**validated_data)
        return produto
        
        


class ProdutoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    marca     = serializers.StringRelatedField()

    class Meta:
        model = Produto
        fields = [
            'id',
            'codigo',
            'categoria',
            'marca',
            'descricao',
            'estoque',
            'estoque_min',
            'preco',
            'genero',
            'tipo',
            'tamanho',
            'criado_em',
            'atualizado_em',
            'ativo'
        ]
        read_only_fields = ['id', 'codigo', 'criado_em', 'atualizado_em']