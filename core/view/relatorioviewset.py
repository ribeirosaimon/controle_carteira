from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.serializers import AcaoSerializers
from compras.models import CompraModel
from vendas.models import VendaModel
from core.classe_acao.acao_obj import Carteira
from core.classe_acao.ir_obj import Imposto_de_renda
from core.classe_acao.acao.calculos import *


class RelatorioViewSet(ModelViewSet):
    serializer_class = AcaoSerializers
    def list(self, request,*args,**kwargs):
        dolar = get_dolar_price()
        imposto = Imposto_de_renda()
        vendas = VendaModel.objects.all()
        ano_info = int(self.request.query_params.get('ano'))
        mes_info = int(self.request.query_params.get('mes'))
        vendas_do_ano = [x for x in vendas if x.data.year == ano_info and x.data.month == mes_info]
        dict_imposto = imposto.isencao_ir(vendas_do_ano, dolar) 
        return Response({'teste':dict_imposto})