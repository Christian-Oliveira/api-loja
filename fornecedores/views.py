from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Fornecedor
from .serializers import FornecedorSerializer

# Create your views here.
class FornecedorListCreateView(generics.ListCreateAPIView):
    """
    Recurso para listar e criar Fornecedor
    """
    serializer_class = FornecedorSerializer

    def list(self, request):
        query = request.GET
        if (query):
            fornecedores = Fornecedor.objects.filter(
                nome__istartswith=query.get('nome'), 
                ativo=True
            )
            if not(fornecedores):
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            fornecedores = Fornecedor.objects.filter(ativo=True)

        serializer = FornecedorSerializer(fornecedores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FornecedorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API para buscar, atualizar e deletar Fornecedor
    """
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer