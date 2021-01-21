from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from carteira.models import VendaModel, CompraModel
from carteira.serializers import CompraSerializers, VendaSerializers

class CompraViewSet(ModelViewSet):
    queryset = CompraModel.objects.all()
    serializer_class = CompraSerializers


class VendaViewSet(ModelViewSet):
    queryset = VendaModel.objects.all()
    serializer_class = VendaSerializers
