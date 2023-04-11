from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from garagem.models import Categoria
from garagem.serializers import CategoriaSerializer
from garagem.models import Marca
from garagem.serializers import MarcaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer