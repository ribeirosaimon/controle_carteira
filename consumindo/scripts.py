import requests
from carteira import *

for dados in carteira:
    url = 'http://127.0.0.1:8000/compra/'
    r = requests.post(url,data=dados)
    print(r.json())
