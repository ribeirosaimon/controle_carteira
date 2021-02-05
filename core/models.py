from django.db import models

class AcaoModel(models.Model):
    acao = models.CharField(max_length=10)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    fechamento = models.DecimalField(max_digits=10, decimal_places=2)
    abertura = models.DecimalField(max_digits=10, decimal_places=2)
    minima = models.DecimalField(max_digits=10, decimal_places=2)
    maxima = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    nacional = models.BooleanField()
    def __str__(self):
        return str(self.data)
