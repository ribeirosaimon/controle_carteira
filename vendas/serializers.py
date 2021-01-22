from rest_framework import serializers
from .models import VendaModel


class VendaSerializers(serializers.ModelSerializer):
    class Meta:
        model = VendaModel
        fields = ('__all__')
