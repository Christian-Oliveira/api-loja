from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Categoria, Marca, Produto
from .serializers import CategoriaSerializer, MarcaSerializer, ProdutoSerializer, ProdutoCreateSerializer

# Create your views here.
#CATEGORIA
class CategoriaList(generics.ListCreateAPIView):
    """
    Recurso para listar e criar Categoria
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Recurso para buscar, atualizar e deletar Categoria
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


#MARCA
class MarcaList(generics.ListCreateAPIView):
    """
    Recurso para listar e criar Marca
    """
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class MarcaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Recurso para buscar, atualizar e deletar Marca
    """
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    # http_method_names = ['get', 'patch', 'delete']

#PRODUTO
class ProdutoList(APIView):
    """
    Recurso para listar e criar Produto
    """
    def get(self, request):
        codigo = request.GET.get('codigo', None)
        descricao = request.GET.get('descricao', None)
        produtosAtivos = Produto.objects.filter(ativo=True)

        if (codigo is not None):
            produtos = produtosAtivos.filter(codigo=codigo)
        elif (descricao is not None):
            produtos = produtosAtivos.filter(descricao__istartswith=descricao)
        else:
            produtos = produtosAtivos

        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProdutoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProdutoDetail(APIView):
    """
    Recurso para buscar, atualizar e deletar Produto
    """
    def get(self, request, pk):
        produto = get_object_or_404(Produto, pk=pk)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    def patch(self, request, pk):
        produto = get_object_or_404(Produto, pk=pk)
        serializer = ProdutoCreateSerializer(produto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        produto = get_object_or_404(Produto, pk=pk)
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
