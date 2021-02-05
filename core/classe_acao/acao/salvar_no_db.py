from core.models import AcaoModel
from datetime import datetime
from .calculos import *
#http://ferramentasdoinvestidor.com.br/financas-quantitativas/como-calcular-a-volatilidade/



def salvar_em_db(carteira,dolar,caixa):
    controle_patrimonio = AcaoModel.objects.all()
    hora_do_dia = int(datetime.now().strftime('%H'))
    if 9 > hora_do_dia or hora_do_dia > 22:
        pass
    else:
        conferindo_acao_no_db(carteira,dolar)
        conferindo_caixa_no_db(caixa)
    



def conferindo_acao_no_db(carteira,dolar):
    patrimonio_db = AcaoModel.objects.all()
    if len(patrimonio_db) == 0:
        for x in carteira:
            fechamento = x['close']
            abertura = x['open']
            minima = x['min']
            maxima = x['max']
            if x['nacional'] == False:
                fechamento = float(fechamento) * dolar
                abertura = float(abertura) * dolar
                minima = float(minima) * dolar
                maxima = float(maxima) * dolar
            patrimonio_obj = AcaoModel(acao=x['acao'],quantidade=x['quantidade'],nacional=x['nacional'],fechamento=fechamento,
                                        abertura=abertura,minima=minima,maxima=maxima,volume=x['volume'],data=x['data'])
            patrimonio_obj.save()
    else:
        for x in carteira:
            acao_no_db = AcaoModel.objects.filter(acao=x['acao'], data=data_de_hoje(data_str=False))
            for y in acao_no_db:
                y = AcaoModel.objects.get(pk=y.pk)
                y.fechamento = x['close']
                y.abertura = x['open']
                y.minima = x['min']
                y.maxima = x['max']
                if x['nacional'] == False:
                    y.fechamento = float(x['close']) * dolar
                    y.abertura = float(x['open']) * dolar
                    y.minima = float(x['min']) * dolar
                    y.maxima = float(x['max']) * dolar
                y.save(update_fields=['quantidade','volume','fechamento','abertura','minima','maxima','data'])

    

def conferindo_caixa_no_db(caixa):
    patrimonio_db = AcaoModel.objects.all()
    if len(patrimonio_db) == 0:
        caixa_obj = AcaoModel(acao='caixa',quantidade=1,nacional=False,fechamento=caixa,
                    abertura=caixa,minima=caixa,maxima=caixa,volume=0,data=data_de_hoje())
        caixa_obj.save()
    else:
        caixa_no_db = AcaoModel.objects.filter(acao='caixa',data=data_de_hoje(data_str=False))
        if len(caixa_no_db) == 0:
            caixa_obj = AcaoModel(acao='caixa',quantidade=1,nacional=False,fechamento=caixa,
                        abertura=caixa,minima=caixa,maxima=caixa,volume=0,data=data_de_hoje())
            caixa_obj.save()
        else:
            for x in caixa_no_db:
                if x.data == data_de_hoje(data_str=False):
                    caixa_no_db  = AcaoModel.objects.get(pk=x.pk)
                    caixa_no_db.quantidade = 1
                    caixa_no_db.nacional = False
                    caixa_no_db.fechamento = caixa
                    caixa_no_db.abertura = caixa
                    caixa_no_db.minima = caixa
                    caixa_no_db.maxima = caixa
                    caixa_no_db.volume = 0
                    caixa_no_db.data = data_de_hoje()
                    caixa_no_db.save(update_fields=['quantidade','volume','fechamento','abertura','minima','maxima','data'])

