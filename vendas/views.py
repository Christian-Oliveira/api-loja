from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import VendaCreateSerializer, VendaSerializer
from .models import Venda, ItemVenda

# Create your views here.
class VendaList(APIView):
    """
    Recurso para listar e criar Vendas
    """
    def get(self, request):
        vendas = Venda.objects.all()
        serializer = VendaSerializer(vendas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendaCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendaDetail(APIView):
    """
    Recurso para buscar, atualizar e deletar Vendas
    """
    def get(self, request, pk):
        venda = get_object_or_404(Venda, pk=pk)
        serializer = VendaSerializer(venda)
        return Response(serializer.data)

    def patch(self, request, pk):
        venda = get_object_or_404(Venda, pk=pk)
        serializer = VendaCreateSerializer(venda, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        venda = get_object_or_404(Venda, pk=pk)
        venda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)