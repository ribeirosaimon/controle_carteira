import requests
from compra import *
from venda import *
from relatorio import *

for dados in compra:
    url = 'http://127.0.0.1:8000/compra/'
    print(dados)
    r = requests.post(url,data=dados)
    print(r.json())

for dados in venda:
    url = 'http://127.0.0.1:8000/venda/'
    print(dados)
    r = requests.post(url,data=dados)
    print(r.json())

for dados in relatorio:
    url = 'http://127.0.0.1:8000/relatoriocompleto/'
    print(dados)
    r = requests.post(url,data=dados)
    print(r.json())

