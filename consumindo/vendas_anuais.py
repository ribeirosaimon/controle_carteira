import csv
import requests
from carteira import *
'''
with open('Vendas_do_ano.csv', 'r') as vendas:

    leitor = csv.reader(vendas)
    url = 'https://safe-island-04942.herokuapp.com/acao/'

    def tratamento_data(numero):
        numero = int(numero)
        if numero < 10:
            numero = f'0{numero}'
        return f'2020-{numero}-01'

    for venda in vendas:
        dados = venda.split(';')
        try:
            dolar = float(dados[7].replace(',','.'))
        except:
            dolar = ''

        dicionario = {
            'ticket':dados[1],
            'quantidade':dados[2],
            'preco_medio':dados[3].replace(',','.'),
            'preco_venda':dados[4].replace(',','.'),
            'data_venda':tratamento_data(dados[0]),
            'vendido':'true',
            'internacional':dados[5].lower(),
            'valor_dolar':dolar
        }
        r = requests.post(url,data=dicionario)
        print(r.json())


for dados in carteira:
    url = 'http://127.0.0.1:8000/compra/'
    r = requests.post(url,data=dados)
    print(r.json())

    

for variacao_diaria in variacao:
    url = 'https://safe-island-04942.herokuapp.com/testepatrimonio/'
    postagem = requests.post(url, data=variacao_diaria)


with open('patrimonio.csv', 'r') as patrimonio:
    url = 'http://127.0.0.1:8000/testepatrimonio/'
    for dados in patrimonio:
        x = dados.split(';')
        dicionario = {'data':f'2020-{x[2]}-01',
                      'patrimonio_br':float(x[0]),
                      'patrimonio_usa':float(x[3]),
                      'patrimonio_total':float(x[0]) + float(x[3])}
        postagem = requests.post(url, data=dicionario)
        print(postagem.json())
        dicionario = {'data':f'2020-{x[2]}-25',
                      'patrimonio_br':float(x[1]),
                      'patrimonio_usa':float(x[4]),
                      'patrimonio_total':float(x[1]) + float(x[4])}
        postagem = requests.post(url, data=dicionario)
        print(postagem.json())

'''