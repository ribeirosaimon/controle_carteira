from django.shortcuts import render
from rest_framework.response import Response
from .models import AcaoModel
from .serializers import AcaoSerializers
from rest_framework.viewsets import ModelViewSet
from carteira.models import CompraModel, VendaModel

class AcaoViewSet(ModelViewSet):
    serializer_class = AcaoSerializers
    def list(self, request,*args,**kwargs):
        compras = CompraModel.objects.all()
        vendas = VendaModel.objects.all()
        print([x.acao for x in compras])
        return Response({'ok':'deu ok'})