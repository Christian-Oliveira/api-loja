from rest_framework import serializers

from .models import Cliente, Endereco

# Campos Obrigatorios
# endereço, bairro, cep, uf, cidade, criado_em, atualizado_em, ativo
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = [
            'logradouro',
            'bairro',
            'cep',
            'numero',
            'uf',
            'cidade',
            'ponto_ref',
            'criado_em',
            'atualizado_em'
        ]

    def validate(self, data):
        cep = len(data['cep'])
        if (cep < 8):
            raise serializers.ValidationError({
                "cep": "Certifique-se de que este campo não tenha menos de 8 caracteres."
            })
        return data

# Campos Obrigatorios
# nome, cpf, sexo, data_nasc, fone, estado_civil, filiação
# status, credito, criado_por, endereço criado_em, atualizado_em, ativo
class ClienteSerializer(serializers.ModelSerializer):
    endereco    = EnderecoSerializer()
    end_entrega = EnderecoSerializer(required=False)

    class Meta:
        model = Cliente
        fields = [
            'id',
            'nome',
            'cpf',
            'rg',
            'sexo',
            'data_nasc',
            'fone',
            'fone_recado',
            'email',
            'estado_civil',
            'conjuge',
            'apelido',
            'filiacao',
            'status',
            'credito',
            'obs',
            'criado_por',
            'criado_em',
            'atualizado_em',
            'ativo',
            'endereco',
            'end_entrega'
        ]
        read_only_fields = ['id', 'criado_por', 'criado_em', 'atualizado_em']

    def validate(self, data):
        cpf = len(data['cpf'])
        if (cpf < 11):
            raise serializers.ValidationError({
                "cpf": "Certifique-se de que este campo não tenha menos de 11 caracteres."
            })
        return data

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        endereco = Endereco.objects.create(**endereco_data)
        if 'end_entrega' in validated_data:
            end_entrega_data = validated_data.pop('end_entrega')
            end_entrega = Endereco.objects.create(**end_entrega_data)
            cliente = Cliente.objects.create(
                endereco=endereco, 
                end_entrega=end_entrega, 
                **validated_data
            )
        else:
            cliente = Cliente.objects.create(
                endereco=endereco, 
                **validated_data
            )
        return cliente

    def update(self, instance, validated_data):
        for field_data in validated_data:
            if not(field_data in ['endereco', 'end_entrega']):
                setattr(instance, field_data, validated_data.get(field_data, getattr(instance, field_data)))

            if 'endereco' in validated_data:
                for field in validated_data['endereco']:
                    setattr(instance.endereco, field, validated_data.get('endereco').get(field, getattr(instance.endereco, field)))
                instance.endereco.save()
                
            if 'end_entrega' in validated_data:
                for field in validated_data['end_entrega']:
                    setattr(instance.end_entrega, field, validated_data.get('end_entrega').get(field, getattr(instance.end_entrega, field)))
                instance.end_entrega.save()
        instance.save()
        return instance