from core.models import AcaoModel
from datetime import datetime
#http://ferramentasdoinvestidor.com.br/financas-quantitativas/como-calcular-a-volatilidade/

def salvar_em_db(info,dolar):
    controle_patrimonio = AcaoModel.objects.all()
    hora_do_dia = int(datetime.now().strftime('%H'))
    hora_do_dia = 12
    if 9 > hora_do_dia or hora_do_dia > 22:
        pass
    else:
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
            if len(controle_patrimonio) == 0:
                patrimonio_obj = AcaoModel(acao=acao,quantidade=quantidade,nacional=nacional,fechamento=fechamento,
                                            abertura=abertura,minima=minima,maxima=maxima,volume=volume,data=data)
                patrimonio_obj.save()
            else:
                acao_no_db = AcaoModel.objects.get(acao=acao)
                acao_no_db.quantidade = quantidade
                acao_no_db.volume = volume
                acao_no_db.fechamento = fechamento
                acao_no_db.abertura = abertura
                acao_no_db.minima = minima
                acao_no_db.maxima = maxima
                acao_no_db.data = data
                acao_no_db.save(update_fields=['quantidade','volume','fechamento','abertura','minima','maxima','data'])

