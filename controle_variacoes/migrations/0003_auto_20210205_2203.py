# Generated by Django 3.1.5 on 2021-02-06 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_variacoes', '0002_auto_20210205_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relatoriocompletomodel',
            name='vol_implicidta',
        ),
        migrations.AddField(
            model_name='relatoriocompletomodel',
            name='vol_implicita_anual',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relatoriocompletomodel',
            name='vol_implicita_diaria',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]