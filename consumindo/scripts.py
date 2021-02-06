import requests
from compra import *
from venda import *
from relatorio import *

for dados in compra:
    url = 'http://127.0.0.1:8000/compra/'
    r = requests.post(url,data=dados)
    print(r.json())

for dados in venda:
    url = 'http://127.0.0.1:8000/venda/'
    r = requests.post(url,data=dados)
    print(r.json())

for dados in relatorio:
    url = 'http://127.0.0.1:8000/relatoriocompleto/'
    r = requests.post(url,data=dados)
    print(r.json())

