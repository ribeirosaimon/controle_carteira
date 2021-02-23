from datetime import datetime, timedelta, date
import requests
import math

def preco_acao(acao, portfolio_carteira):
    for valor in portfolio_carteira:
        if valor['acao'] == acao:
            preco_no_dia = valor['info'][0]['dados']['close']
            return round(preco_no_dia,2)
            


def info_das_acoes(acao, nacional=True):
    informacao_retorno = []
    data = str(date.today())
    url_acao = acao
    if nacional == True:
        url_acao = f'{acao}.sa'
    url = f'https://query2.finance.yahoo.com/v8/finance/chart/{url_acao}?symbol={url_acao}&period1={data_utc(data, mes_passado=True)}&period2={data_utc(data, mes_passado=False)}&interval=1d&includePrePost=true&events=div%2Csplit'
    info = requests.get(url)
    fechamento = info.json()['chart']['result'][0]['indicators']['quote'][0]['close']
    abertura = info.json()['chart']['result'][0]['indicators']['quote'][0]['open']
    minima = info.json()['chart']['result'][0]['indicators']['quote'][0]['low']
    maxima = info.json()['chart']['result'][0]['indicators']['quote'][0]['high']
    volume = info.json()['chart']['result'][0]['indicators']['quote'][0]['volume']
    data = info.json()['chart']['result'][0]['timestamp']
    for index in range(len(fechamento)):
        try:
            dicionario = {
                            'data':data_iso(data[index]),
                            'dados':
                                {
                                    'close':round(fechamento[index],2),
                                    'open':round(abertura[index],2),
                                    'min':round(minima[index],2),
                                    'max':round(maxima[index],2),
                                    'volume':round(volume[index],2),
                                }
                        }            
            informacao_retorno.append(dicionario)
        except:
            pass
    informacao_retorno = informacao_retorno[::-1]
    dict_info = {
                'acao':acao,
                'info':informacao_retorno}
    return dict_info

def calculo_preco_medio(pm1, qtd1, pm2, qtd2):
    valor_de_aquisicao_1 = pm1 * qtd1
    valor_de_aquisicao_2 = pm2 * qtd2
    posicao = qtd1 + qtd2
    preco_medio = (valor_de_aquisicao_1 + valor_de_aquisicao_2) / posicao
    return round(preco_medio,2)


def data_utc(data_str, mes_passado = False):
    data = datetime.strptime(data_str, '%Y-%m-%d').date()
    data = data - timedelta(hours=-3)
    if mes_passado == True:
        data = data - timedelta(days=92)
    data = data - datetime(1970, 1, 1).date()
    return int(data.total_seconds())

def data_de_hoje(data_str=True,delta=0):
    hora_do_dia = int(datetime.now().strftime('%H'))
    data = date.today()
    if delta == 0:
        if hora_do_dia < 9:
            data = data - timedelta(days=1)
        if data_str == True:
            return str(data)
        else:
            return data
    if delta > 0:
        if hora_do_dia < 9:
            tempo = 1 + delta
            data = data - timedelta(days=tempo)
        if data_str == True:
            return str(data - timedelta(days=delta))
        else:
            return data - timedelta(days=delta)


def data_iso(data_str):
    UTC_datetime_converted = datetime.utcfromtimestamp(data_str).date().strftime("%Y-%m-%d")
    return UTC_datetime_converted


def get_dolar_price():
    endpoint  = 'https://economia.awesomeapi.com.br/json/daily/USD-BRL/2'
    resposta = requests.request('GET', endpoint)
    dolar_do_dia =  float(resposta.json()[0]['ask'])
    #dolar_ultimo_dia = float(resposta.json()[1]['ask'])
    return dolar_do_dia


def calculo_de_volume(volume_medio,volume_diario,horario_comercial=8,inicio_expediente=10):
    hora_do_dia = int(datetime.now().strftime('%H'))
    minuto_do_dia = int(datetime.now().strftime('%M'))
    if minuto_do_dia > 45:
        hora_do_dia = hora_do_dia + 1
    tempo_de_expediente = hora_do_dia - inicio_expediente
    if 0 > tempo_de_expediente or tempo_de_expediente > 8:
        tempo_de_expediente = 8
    volume_medio_por_hora = int(round(volume_medio / horario_comercial,0))
    volume_medio_do_dia = volume_medio_por_hora * tempo_de_expediente
    if volume_diario != 0:
        porcentagem_diferenca = round((volume_medio_do_dia/ volume_diario)-1,2)
    else:
        porcentagem_diferenca = 0
    dict_volume = {'volume':volume_diario,
                    'dados':{'avg_vol':volume_medio,
                             'high':'none',
                             'percent':porcentagem_diferenca}}

    if volume_diario > volume_medio_do_dia:
        dict_volume['dados']['high'] = True
    else:
        dict_volume['dados']['high'] = False
    return dict_volume


def calculo_variacao_patrimonial(db, caixa):
    dia_da_semana = date.today().weekday()
    hoje = data_de_hoje(data_str=False)
    if dia_da_semana == 5:
        hoje = data_de_hoje(data_str=False,delta=1)
    if dia_da_semana == 6:
        hoje = data_de_hoje(data_str=False,delta=2)
    caixa_total = caixa[0]['caixa_br'] + caixa[1]['caixa_usa']
    carteira_no_dia = db.objects.all()
    fechamento = round(sum([float(x.fechamento) * float(x.quantidade) for x in carteira_no_dia if x.data == hoje]) + caixa_total,2)
    abertura = round(sum([float(x.abertura) * float(x.quantidade) for x in carteira_no_dia if x.data == hoje])+ caixa_total,2)
    minima = round(sum([float(x.minima) * float(x.quantidade) for x in carteira_no_dia if x.data == hoje])+caixa_total,2)
    maxima = round(sum([float(x.maxima) * float(x.quantidade) for x in carteira_no_dia if x.data == hoje])+caixa_total,2)
    volume = round(sum([float(x.volume) for x in carteira_no_dia if x.data == hoje]),0) / 1000000
    dict_variacao = {'variacao_diaria':
                                    {
                                        'data':data_de_hoje(),
                                        'fechamento':fechamento,
                                        'abertura':abertura,
                                        'minima':minima,
                                        'maxima':maxima,
                                        'volume':volume,
                                    }
                    }
    return dict_variacao

def patrimonio_hoje_ontem(AcaoModel):
    lista_do_dia = []
    fechamento,abertura,minima,maxima,volume = [],[],[],[],[]
    fechamento_ontem,abertura_ontem,minima_ontem,maxima_ontem,volume_ontem = [],[],[],[],[]
    todas_acoes = AcaoModel.objects.order_by('-data')
    teste = [lista_do_dia.append(x.data) for x in todas_acoes if x.data not in lista_do_dia]
    hoje = lista_do_dia[0]
    ontem = lista_do_dia[1]
    for x in todas_acoes:
        if x.data == hoje:
            fechamento.append(x.fechamento * x.quantidade)
            abertura.append(x.abertura * x.quantidade)
            minima.append(x.minima * x.quantidade)
            maxima.append(x.maxima * x.quantidade)
            volume.append(x.volume)
        if x.data == ontem:
            fechamento_ontem.append(x.fechamento * x.quantidade)
            abertura_ontem.append(x.abertura * x.quantidade)
            minima_ontem.append(x.minima * x.quantidade)
            maxima_ontem.append(x.maxima * x.quantidade)
            volume_ontem.append(x.volume)

    dict_hoje = montando_dict_volatilidade(fechamento,abertura,minima,maxima,volume,dia_de_hoje=hoje)
    dict_ontem = montando_dict_volatilidade(fechamento_ontem,abertura_ontem,minima_ontem,maxima_ontem,volume_ontem,dia_de_hoje=ontem)
    return dict_hoje, dict_ontem

def montando_dict_volatilidade(*dados,dia_de_hoje='None'):
    lista_dados = []
    for x in dados:
        soma = lista_dados.append(round(sum(x),2))
    dict_retorno = {'dia':dia_de_hoje,
                    'fechamento':lista_dados[0],
                    'abertura':lista_dados[1],
                    'minima':lista_dados[2],
                    'maxima':lista_dados[3],
                    'volume':lista_dados[4]
                    }
    return dict_retorno

def variacao_da_carteira(dados):
    valor_variacao = round((dados[0]['fechamento'] / dados[1]['fechamento']) - 1,4)
    return valor_variacao

def volatilidade_implicita_da_carteira(dados):
    vol_diaria = float((dados[0]['fechamento'] - dados[1]['fechamento']) / dados[1]['fechamento'])
    raiz = math.sqrt(252)
    vol_anual = vol_diaria * raiz
    dict_volatilidade = {'volatilidade_diaria':round(vol_diaria,4),
                        'volatilidade_anual':round(vol_anual,4)}
    return dict_volatilidade