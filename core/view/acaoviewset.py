from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.serializers import AcaoSerializers
from compras.models import CompraModel
from vendas.models import VendaModel
from core.classe_acao.acao_obj import Carteira

class AcaoViewSet(ModelViewSet):
    serializer_class = AcaoSerializers
    def list(self, request,*args,**kwargs):
        compras = CompraModel.objects.all() 
        vendas = VendaModel.objects.all()
        portfolio = Carteira()
        portfolio.reset_carteira()
        lista_compras = [portfolio.comprar(x.acao,float(x.preco_medio),float(x.quantidade),x.nacional,x.data) for x in compras]
        lista_vendas = [portfolio.vender(x.acao,float(x.preco_medio),float(x.quantidade),nacional=x.nacional,data=x.data) for x in vendas]
        portfolio.inicializar_carteira()
        erro = [x for x in lista_vendas if x != True]
        if len(erro) != 0:
            return Response({'error':erro})
        return Response({'carteira':portfolio.portfolio_carteira()})