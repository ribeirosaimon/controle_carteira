from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.serializers import AcaoSerializers
from core.models import AcaoModel
from compras.models import CompraModel
from vendas.models import VendaModel
from core.classe_acao.acao_obj import Carteira
from core.classe_acao.ir_obj import Imposto_de_renda
from core.classe_acao.acao.info_carteira import *
from core.classe_acao.acao.calculos import *
from core.classe_acao.acao.salvar_no_db import *

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
        lista_vendas = [portfolio.vender(x.acao,float(x.preco_venda),float(x.preco_medio),
                        float(x.quantidade),nacional=x.nacional,data=x.data, dolar=float(x.dolar)) for x in vendas]
        vendas_do_mes = [x for x in vendas if x.data.year == ano_info and x.data.month == mes_info]
        [portfolio.caixa(float(x.preco_medio), x.nacional) for x in compras if x.acao == 'caixa']
        dict_imposto = imposto.isencao_ir(vendas_do_mes, dolar) 
        ir_devendo = imposto.ir_devido(portfolio.relatorio_vendas())


        portfolio.inicializar_carteira()
        
        caixa = portfolio.info_caixa(dolar)
        
        informacoes_da_carteira = info_carteira(portfolio, dolar, caixa)
        
        variacao_do_patrimonio = patrimonio_hoje_ontem(AcaoModel)
        
        portfolio.variacao_da_carteira(dolar)
        dict_carteira_completo={'patrimonio':{'patrimonio_total':portfolio.patrimonio(dolar),
                         'patrimonio_br':portfolio.patrimonio(dolar,nacional=True),
                         'patrimonio_usa':portfolio.patrimonio(dolar,nacional=False),
                         'lucro_carteira_br':portfolio.lucro_carteira(dolar,nacional=True,acao=None),
                         'lucro_carteira_usa':portfolio.lucro_carteira(dolar,nacional=False,acao=None),
                         'variacao_carteira':calculo_variacao_patrimonial(AcaoModel, caixa),
                         'volatilidade_implicita_carteira':volatilidade_implicita_da_carteira(variacao_do_patrimonio),
                         'variacao_da_carteira':variacao_da_carteira(variacao_do_patrimonio),
                         'caixa':caixa},
                         'ir':{'isencao':dict_imposto,
                                'ir_devido':ir_devendo},
                        'info':informacoes_da_carteira}
        salvando_relatorio_completo(**dict_carteira_completo)
        return Response(dict_carteira_completo)