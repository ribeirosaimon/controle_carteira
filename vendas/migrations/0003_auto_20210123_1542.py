# Generated by Django 3.1.5 on 2021-01-23 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_vendamodel_dolar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendamodel',
            name='dolar',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
