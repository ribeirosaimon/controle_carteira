from django.shortcuts import render
from rest_framework import viewsets
from core.serializers import AcaoSerializers
from core.models import AcaoModel
from core.classe_acao.acao_obj import Carteira
from core.classe_acao.ir_obj import Imposto_de_renda
from core.classe_acao.acao.calculos import *


class PatrimonioViewSet(viewsets.ModelViewSet):
    queryset = AcaoModel.objects.all()
    serializer_class = AcaoSerializers