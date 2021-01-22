from django.shortcuts import render
from rest_framework.response import Response
from .models import AcaoModel
from .serializers import AcaoSerializers
from rest_framework.viewsets import ModelViewSet
from carteira.models import CompraModel, VendaModel
from .classe_acao.acao_obj import Carteira

class AcaoViewSet(ModelViewSet):
    serializer_class = AcaoSerializers
    def list(self, request,*args,**kwargs):
        compras = CompraModel.objects.all()
        vendas = VendaModel.objects.all()
        portfolio = Carteira()
        for acao in compras:
            portfolio.comprar(acao['acao'],acao['preco_medio'], acao['quantidade'], acao['nacional'],acao['data'])


        return Response()