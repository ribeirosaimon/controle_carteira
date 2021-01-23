from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.serializers import AcaoSerializers
from compras.models import CompraModel
from vendas.models import VendaModel
from core.classe_acao.acao_obj import Carteira
from core.classe_acao.ir_obj import Imposto_de_renda
from core.classe_acao.acao.info_carteira import *
from core.classe_acao.acao.calculos import *

class AcaoViewSet(ModelViewSet):
    serializer_class = AcaoSerializers
    def list(self, request,*args,**kwargs):
        dolar = get_dolar_price()
        ano_info = int(self.request.query_params.get('ano'))
        mes_info = int(self.request.query_params.get('mes'))
        compras = CompraModel.objects.all() 
        vendas = VendaModel.objects.all()
        imposto = Imposto_de_renda()
        portfolio = Carteira()
        portfolio.reset_carteira()
        lista_compras = [portfolio.comprar(x.acao,float(x.preco_medio),float(x.quantidade),x.nacional,x.data) for x in compras if x.acao != 'caixa']
        lista_vendas = [portfolio.vender(x.acao,float(x.preco_medio),float(x.quantidade),nacional=x.nacional,data=x.data) for x in vendas]
        vendas_do_mes = [x for x in vendas if x.data.year == ano_info and x.data.month == mes_info]
        caixa = [portfolio.caixa(float(x.preco_medio), x.nacional) for x in compras if x.acao == 'caixa']

        dict_imposto = imposto.isencao_ir(vendas_do_mes, dolar) 
        ir_devendo = imposto.ir_devido(portfolio.relatorio_vendas(),dolar)

        portfolio.inicializar_carteira()
        informacoes_da_carteira = info_carteira(portfolio, dolar)
        erro = [x for x in lista_vendas if x != True]
        if len(erro) != 0:
            return Response({'error':erro})
        return Response({'carteira':portfolio.portfolio_carteira(),
                         'ir':{'isencao':dict_imposto,
                                'ir_devido':ir_devendo},
                        'info':informacoes_da_carteira})
