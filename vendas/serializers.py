from rest_framework import serializers

from produtos.serializers import ProdutoSerializer
from .models import Venda, ItemVenda

class ItemVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVenda
        fields = (
            'produto',
            'venda',
            'quantidade',
            'preco_unitario',
            'preco_total',
        )

        read_only_fields = ['venda']


class VendaCreateSerializer(serializers.ModelSerializer):
    produtos = ItemVendaSerializer(many=True, required=True)

    class Meta:
        model = Venda
        fields = (
            'cliente',
            'vendedor',
            'caixa',
            'produtos',
            'valor_total',
            'desconto',
            'forma_pagamento',
            'valor_pago',
            'qtd_parcelas',
            'valor_parcelas',
            'venc_parcelas',
            'status'
        )

    def create(self, validated_data):
        produtos_venda = validated_data.pop('produtos')
        venda = Venda.objects.create(**validated_data)
        produtos = [ItemVenda(venda=venda, **item) for item in produtos_venda]
        ItemVenda.objects.bulk_create(produtos)
        return venda
            


class VendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venda
        fields = (
            'id',
            'cliente',
            'vendedor',
            'caixa',
            'produtos',
            'valor_total',
            'desconto',
            'forma_pagamento',
            'valor_pago',
            'qtd_parcelas',
            'valor_parcelas',
            'venc_parcelas',
            'status',
            'criado_em',
            'atualizado_em',
            'ativo'
        )
        read_only_fields = ['id', 'criado_em', 'atualizado_em']