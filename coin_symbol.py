from hashlib import new
from operator import contains
from tokenize import Name
from typing import ItemsView
import requests

url = 'https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

params = {
        'start': 1,
        'limit': 4000
    }
r = requests.get(url, params=params)
data = r.json()

coin_name=[]
coin_symbol=[]
coin_dictionary={}

data=data['data']

def get_coin_symbols(coin_name):
    for d in data:
        symbol=d['symbol']
        if symbol == coin_name:
            name=d['name']
            coin_dictionary[name]=symbol
            print(coin_dictionary)

for d in data:
    symbol=d['symbol']
    name=d['name']
    coin_dictionary[name]=symbol

    # print(type(symbol), symbol, type(name), name)
    # coin_name.append(name)
    # coin_symbol.append(symbol)

