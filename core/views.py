from django.shortcuts import render
from rest_framework.response import Response
from .models import AcaoModel
from .serializers import AcaoSerializers
from rest_framework.viewsets import ModelViewSet
from compras.models import CompraModel
from vendas.models import VendaModel
from .classe_acao.acao_obj import Carteira

class AcaoViewSet(ModelViewSet):
    serializer_class = AcaoSerializers
    def list(self, request,*args,**kwargs):
        compras = CompraModel.objects.all() 
        vendas = VendaModel.objects.all()
        portfolio = Carteira()
        [portfolio.comprar(x.acao,float(x.preco_medio),float(x.quantidade),x.nacional,x.data) for x in compras]
        [portfolio.vender(x.acao,float(x.preco_medio),float(x.quantidade),nacional=x.nacional,data=x.data) for x in vendas]
        portfolio.inicializar_carteira()
        return Response({'carteira':portfolio.portfolio_carteira()})