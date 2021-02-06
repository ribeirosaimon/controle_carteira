from rest_framework import serializers
from .models import RelatorioCompletoModel

class RelatorioCompletoSerializers(serializers.ModelSerializer):
    class Meta:
        model = RelatorioCompletoModel
        fields = ('__all__')