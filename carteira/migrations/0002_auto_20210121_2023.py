# Generated by Django 3.1.5 on 2021-01-21 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carteira', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compramodel',
            name='nacional',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendamodel',
            name='nacional',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
