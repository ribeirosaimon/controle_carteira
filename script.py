import requests

url = 'http://127.0.0.1:8000/patrimonio/'

r = requests.get(url).json()
for x in r:
    requests.delete(f'{url}{x["id"]}')

acoes = [
        {
            "acao": "caixa",
            "quantidade": "1.00",
            "fechamento": "98.92",
            "abertura": "98.92",
            "minima": "98.92",
            "maxima": "98.92",
            "volume": "0.00",
            "data": "2021-02-04",
            "nacional": False
        },
        {
            "id": 511,
            "acao": "cogn3",
            "quantidade": "790.00",
            "fechamento": "4.62",
            "abertura": "4.75",
            "minima": "4.58",
            "maxima": "4.76",
            "volume": "31580900.00",
            "data": "2021-01-04",
            "nacional": True
        },
        {
            "id": 512,
            "acao": "ctnm4",
            "quantidade": "600.00",
            "fechamento": "5.64",
            "abertura": "5.74",
            "minima": "5.64",
            "maxima": "5.84",
            "volume": "19700.00",
            "data": "2021-02-04",
            "nacional": True
        },
        {
            "id": 513,
            "acao": "rlog3",
            "quantidade": "200.00",
            "fechamento": "19.90",
            "abertura": "19.65",
            "minima": "19.43",
            "maxima": "20.00",
            "volume": "406200.00",
            "data": "2021-02-04",
            "nacional": True
        },
        {
            "id": 514,
            "acao": "sapr4",
            "quantidade": "1100.00",
            "fechamento": "4.37",
            "abertura": "4.44",
            "minima": "4.33",
            "maxima": "4.45",
            "volume": "5100400.00",
            "data": "2021-02-04",
            "nacional": True
        },
        {
            "id": 515,
            "acao": "mmm",
            "quantidade": "14.00",
            "fechamento": "949.25",
            "abertura": "942.82",
            "minima": "940.73",
            "maxima": "950.27",
            "volume": "1833000.00",
            "data": "2021-02-04",
            "nacional": False
        },
        {
            "id": 516,
            "acao": "ko",
            "quantidade": "38.00",
            "fechamento": "262.69",
            "abertura": "262.42",
            "minima": "260.87",
            "maxima": "263.01",
            "volume": "20564300.00",
            "data": "2021-02-04",
            "nacional": False
        },
        {
            "id": 517,
            "acao": "irbr3",
            "quantidade": "300.00",
            "fechamento": "7.13",
            "abertura": "7.26",
            "minima": "7.10",
            "maxima": "7.34",
            "volume": "18180000.00",
            "data": "2021-02-04",
            "nacional": True
        },
        {
            "id": 518,
            "acao": "tcsa3",
            "quantidade": "400.00",
            "fechamento": "9.06",
            "abertura": "9.14",
            "minima": "9.01",
            "maxima": "9.33",
            "volume": "986000.00",
            "data": "2021-02-04",
            "nacional": True
        },
        {
            "id": 519,
            "acao": "meli",
            "quantidade": "2.15",
            "fechamento": "10148.35",
            "abertura": "10210.80",
            "minima": "9969.90",
            "maxima": "10250.08",
            "volume": "370000.00",
            "data": "2021-02-04",
            "nacional": False
        }
    ]

#for y in acoes:
 #   requests.post(url,data=y)