from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from vendas.models import VendaModel
from vendas.serializers import VendaSerializers


class VendaViewSet(ModelViewSet):
    queryset = VendaModel.objects.all()
    serializer_class = VendaSerializers
