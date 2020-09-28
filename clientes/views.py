from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404

from .models import Cliente
from .serializers import ClienteSerializer, EnderecoSerializer

###CLIENTES
class ClienteListCreateView(APIView):
    """
    Recurso para listar e criar Cliente
    """
    def get(self, request):
        query = request.GET
        if (query):
            clientes = Cliente.objects.filter(
                nome__istartswith=query.get('nome'), 
                ativo=True
            )
            if not(clientes):
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            clientes = Cliente.objects.filter(ativo=True)

        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(criado_por=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ClienteDetailView(APIView):
    """
    API para buscar, atualizar e deletar Cliente
    """
    def get(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    def put(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        serializer = ClienteSerializer(cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        try:
            if cliente.endereco is not None:
                cliente.endereco.delete()
            if cliente.end_entrega is not None:
                cliente.end_entrega.delete()
            cliente.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as error:
            raise ValidationError(error)

        