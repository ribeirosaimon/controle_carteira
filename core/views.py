from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.models import AcaoModel
from core.serializers import AcaoSerializers

class AcaoModelViewSet(ModelViewSet):
    queryset = AcaoModel.objects.all()
    serializer_class = AcaoSerializers

