from rest_framework import serializers
from .models import CompraModel, VendaModel

class CompraSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompraModel
        fields = ('__all__')

class VendaSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompraModel
        fields = ('__all__')
