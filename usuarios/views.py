from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from .serializers import UsuarioSerializer
from .models import Perfil

# Create your views here.
###USUARIOS
class UsuariosGenericView(generics.ListCreateAPIView):
    """
    API para listar e criar Usuario
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

    def list(self, request):
        query = request.GET
        if (query):
            usuarios = User.objects.filter(
                username__istartswith=query.get('username'), 
                is_active=True
            )
            if not(usuarios):
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            usuarios = User.objects.filter(is_active=True)

        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        cpfExist = Perfil.objects.filter(cpf=self.request.data['cpf'])
        if cpfExist.exists():
            raise ValidationError({ "cpf": ["Um usuário com este CPF já existe."] })
        serializer.save()



class UsuarioGenericView(generics.RetrieveUpdateDestroyAPIView):
    """
    API para buscar, atualizar e deletar Usuario
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer