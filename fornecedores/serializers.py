from rest_framework import serializers

from .models import Fornecedor


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = [
            'nome',
            'cnpj',
            'fone',
            'email',
            'endereco'
        ]

    def validate(self, data):
        cnpj = len(data['cnpj'])
        if (cnpj < 14):
            raise serializers.ValidationError({
                "cnpj": "Certifique-se de que este campo não tenha menos de 14 caracteres."
            })
        return data