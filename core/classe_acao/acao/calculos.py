from datetime import datetime, timedelta, date
import requests

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
    fechamento = info.json()['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
    abertura = info.json()['chart']['result'][0]['indicators']['quote'][0]['open']
    minima = info.json()['chart']['result'][0]['indicators']['quote'][0]['low']
    maxima = info.json()['chart']['result'][0]['indicators']['quote'][0]['high']
    volume = info.json()['chart']['result'][0]['indicators']['quote'][0]['volume']
    data = info.json()['chart']['result'][0]['timestamp']
    for index in range(len(fechamento)):
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
    volume_medio_por_hora = int(round(volume_medio / horario_comercial,0))
    volume_medio_do_dia = volume_medio_por_hora * tempo_de_expediente
    porcentagem_diferenca = round((volume_medio_do_dia/ volume_diario)-1,2)
    dict_volume = {'volume':volume_diario,
                    'dados':{'avg_vol':volume_medio,
                             'high':'none',
                             'percent':porcentagem_diferenca}}

    if volume_diario > volume_medio_do_dia:
        dict_volume['dados']['high'] = True
    else:
        dict_volume['dados']['high'] = False
    return dict_volume