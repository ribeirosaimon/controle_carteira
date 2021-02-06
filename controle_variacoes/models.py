from django.db import models

# Create your models here.

class RelatorioCompletoModel(models.Model):
    patrimonio_total = models.DecimalField(max_digits=10, decimal_places=2)
    patrimonio_br = models.DecimalField(max_digits=10, decimal_places=2)
    patrimonio_usa = models.DecimalField(max_digits=10, decimal_places=2)
    lucro_br = models.DecimalField(max_digits=10, decimal_places=2)
    lucro_usa = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    abertura = models.DecimalField(max_digits=10, decimal_places=2)
    fechamento = models.DecimalField(max_digits=10, decimal_places=2)
    minima = models.DecimalField(max_digits=10, decimal_places=2)
    maxima = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.DecimalField(max_digits=20, decimal_places=2)
    vol_implicita_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    vol_implicita_anual = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)
