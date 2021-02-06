from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import RelatorioCompletoModel
from .serializers import RelatorioCompletoSerializers


class RelatorioCompletoViewSet(ModelViewSet):
    queryset = RelatorioCompletoModel.objects.all()
    serializer_class = RelatorioCompletoSerializers
