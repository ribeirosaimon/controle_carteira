# Generated by Django 3.1.5 on 2021-02-06 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_variacoes', '0003_auto_20210205_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relatoriocompletomodel',
            name='nacional',
        ),
    ]
