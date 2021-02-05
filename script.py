import requests

url = 'http://127.0.0.1:8000/patrimonio/'

r = requests.get(url).json()
for x in r:
    requests.delete(f'{url}{x["id"]}')