from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from garagem.models import Categoria
from garagem.serializers import CategoriaSerializer
from garagem.models import Marca
from garagem.serializers import MarcaSerializer
from garagem.models import Acessorio
from garagem.serializers import AcessorioSerializer
from garagem.models import Cor
from garagem.serializers import CorSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer


