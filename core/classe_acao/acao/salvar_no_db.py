from core.models import AcaoModel
from datetime import datetime
from .calculos import *
from controle_variacoes.models import RelatorioCompletoModel



def salvar_em_db(carteira,dolar,caixa):
    controle_patrimonio = AcaoModel.objects.all()
    hora_do_dia = int(datetime.now().strftime('%H'))
    dia_da_semana = date.today().weekday()
    if dia_da_semana == 5 or dia_da_semana == 6:
        return
    if 9 > hora_do_dia or hora_do_dia > 22:
        return
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
            if len(acao_no_db) == 0:
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

def salvando_relatorio_completo(**dados):
    dia_da_semana = date.today().weekday()
    if dia_da_semana == 5 or dia_da_semana == 6:
        pass
    else:
        relatoriomodel = RelatorioCompletoModel.objects.all()
        patrimonio_total = dados['patrimonio']['patrimonio_total']
        patrimonio_br = dados['patrimonio']['patrimonio_br']
        patrimonio_usa = dados['patrimonio']['patrimonio_usa']
        lucro_carteira_br = dados['patrimonio']['lucro_carteira_br']
        lucro_carteira_usa = dados['patrimonio']['lucro_carteira_usa']
        data = dados['patrimonio']['variacao_carteira']['variacao_diaria']['data']
        fechamento = dados['patrimonio']['variacao_carteira']['variacao_diaria']['fechamento']
        abertura = dados['patrimonio']['variacao_carteira']['variacao_diaria']['abertura']
        minima = dados['patrimonio']['variacao_carteira']['variacao_diaria']['minima']
        maxima = dados['patrimonio']['variacao_carteira']['variacao_diaria']['maxima']
        volume = dados['patrimonio']['variacao_carteira']['variacao_diaria']['volume']
        vol_diaria = dados['patrimonio']['volatilidade_implicita_carteira']['volatilidade_diaria']
        vol_anual = dados['patrimonio']['volatilidade_implicita_carteira']['volatilidade_anual']
        if len(relatoriomodel) == 0:
            relatorioobj = RelatorioCompletoModel(patrimonio_total=patrimonio_total,patrimonio_br=patrimonio_br,patrimonio_usa=patrimonio_usa,lucro_br=lucro_carteira_br,lucro_usa=lucro_carteira_usa,data=data,abertura=abertura,fechamento=fechamento,minima=minima,maxima=maxima,volume=volume,vol_implicita_diaria=vol_diaria,vol_implicita_anual=vol_anual)
            relatorioobj.save()
        else:
            try:
                relatorio_do_dia = RelatorioCompletoModel.objects.get(data=data_de_hoje(data_str=True))
                if relatorio_do_dia.data == data_de_hoje(data_str=False):
                    relatorio_do_dia.patrimonio_total = patrimonio_total
                    relatorio_do_dia.patrimonio_br = patrimonio_br
                    relatorio_do_dia.patrimonio_usa = patrimonio_usa
                    relatorio_do_dia.lucro_carteira_br = lucro_carteira_br
                    relatorio_do_dia.lucro_carteira_usa = lucro_carteira_usa
                    relatorio_do_dia.fechamento = fechamento
                    relatorio_do_dia.abertura = abertura
                    relatorio_do_dia.minima = minima
                    relatorio_do_dia.maxima = maxima
                    relatorio_do_dia.volume = volume
                    relatorio_do_dia.vol_diaria = vol_diaria
                    relatorio_do_dia.vol_anual = vol_anual
                    relatorio_do_dia.save()
            except:
                    relatorioobj = RelatorioCompletoModel(patrimonio_total=patrimonio_total,patrimonio_br=patrimonio_br,patrimonio_usa=patrimonio_usa,lucro_br=lucro_carteira_br,lucro_usa=lucro_carteira_usa,data=data,abertura=abertura,fechamento=fechamento,minima=minima,maxima=maxima,volume=volume,vol_implicita_diaria=vol_diaria,vol_implicita_anual=vol_anual)
                    relatorioobj.save()
            