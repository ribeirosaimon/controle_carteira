from django.db import models

class AcaoModel(models.Model):
    acao = models.CharField(max_length=10)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    preco_medio = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    def __str__(self):
        return str(self.data)
