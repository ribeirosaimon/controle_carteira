from rest_framework import serializers
from .models import AcaoModel

class AcaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = AcaoModel
        fields = ('__all__')