from core.models import AcaoModel
from datetime import datetime
from .calculos import *
#http://ferramentasdoinvestidor.com.br/financas-quantitativas/como-calcular-a-volatilidade/

def conferindo_acao_no_db(carteira):
    patrimonio_db = AcaoModel.objects.all()
    print(patrimonio_db)
    for acao in carteira:
        teste = AcaoModel.objects.get(acao=acao['acao'])
        print(teste)


def salvar_em_db(carteira,dolar,caixa):
    controle_patrimonio = AcaoModel.objects.all()
    hora_do_dia = int(datetime.now().strftime('%H'))
    if 9 > hora_do_dia or hora_do_dia > 22:
        pass
    else:
        # se o db estiver vazio
        if len(controle_patrimonio) == 0:
            pass

        conferindo_acao_no_db(carteira)
        '''
        db = AcaoModel.objects.all()
        caixa_db = [x for x in db if x.acao == 'caixa']
        if len(caixa_db) == 0:
            caixa_obj = AcaoModel(acao='caixa',quantidade=1,nacional=False,fechamento=caixa,
                                abertura=caixa,minima=caixa,maxima=caixa,volume=0,data=data_de_hoje())
            caixa_obj.save()

        for valor in caixa_db:
            if valor.data != data_de_hoje():
                caixa_obj = AcaoModel(acao='caixa',quantidade=1,nacional=False,fechamento=caixa,
                                    abertura=caixa,minima=caixa,maxima=caixa,volume=0,data=data_de_hoje())
                caixa_obj.save()
            else:
                hoje = data_de_hoje()
                caixa_existente = AcaoModel.objects.get(acao='caixa')
                caixa_existente.quantidade = 1
                caixa_existente.nacional = False
                caixa_existente.fechamento = caixa
                caixa_existente.abertura = caixa
                caixa_existente.minima = caixa
                caixa_existente.maxima = caixa
                caixa_existente.volume = 14564
                caixa_existente.data = data_de_hoje()
                caixa_existente.save(update_fields=['quantidade','volume','fechamento','abertura','minima','maxima','data'])

        for x in info:
            acao = x['acao']
            quantidade = x['quantidade']
            nacional = x['nacional']
            volume = x['volume']
            fechamento = x['close']
            abertura = x['open']
            minima = x['min']
            maxima = x['max']
            data = x['data']
 
            if nacional == False:
                fechamento = fechamento * dolar
                abertura = abertura * dolar
                minima = minima * dolar
                maxima = maxima * dolar

            if len(controle_patrimonio) == 1:
                patrimonio_obj = AcaoModel(acao=acao,quantidade=quantidade,nacional=nacional,fechamento=fechamento,
                                            abertura=abertura,minima=minima,maxima=maxima,volume=volume,data=data)
                patrimonio_obj.save()
            else:
                carteira_do_dia = [x for x in db if x.data != data_de_hoje()]
                print(carteira_do_dia)
                if data == data_de_hoje():
                    print('passou aqui')
                    acao_no_db = AcaoModel.objects.get(acao=acao)
                    acao_no_db.quantidade = quantidade
                    acao_no_db.volume = volume
                    acao_no_db.fechamento = fechamento
                    acao_no_db.abertura = abertura
                    acao_no_db.minima = minima
                    acao_no_db.maxima = maxima
                    acao_no_db.data = data
                    acao_no_db.save(update_fields=['quantidade','volume','fechamento','abertura','minima','maxima','data'])
        '''

    