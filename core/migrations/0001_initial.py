# Generated by Django 3.1.5 on 2021-02-05 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcaoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acao', models.CharField(max_length=10)),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preco_medio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateField()),
                ('nacional', models.BooleanField()),
            ],
        ),
    ]
