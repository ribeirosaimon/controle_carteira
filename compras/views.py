from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from compras.models import CompraModel
from compras.serializers import CompraSerializers

class CompraViewSet(ModelViewSet):
    queryset = CompraModel.objects.all()
    serializer_class = CompraSerializers

