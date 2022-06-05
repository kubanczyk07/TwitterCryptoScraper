# import requests

# url = 'https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# for start in range(1, 20000, 5000):
#     print(start)
#     params = {
#         'start': start,
#         'limit': 5000,
#     }

#     r = requests.get(url, params=params)
#     data = r.json()
    
# for number, item in enumerate(data['data']):
#     print(f"{start+number:4} | {item['symbol']:5} | {item['date_added'][:10]}")
from hashlib import new
from operator import contains
from tokenize import Name
from typing import ItemsView
import requests

# creating function

def coin_dictionary():
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

    for d in data:
        symbol=d['symbol']
        name=d['name']
        coin_dictionary[name]=symbol
    return(coin_dictionary)

# print(coin_dictionary())

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

for d in data:
    symbol=d['symbol']
    name=d['name']
    coin_dictionary[name]=symbol
print(coin_dictionary)

if 'NEAR Protocol' in coin_dictionary:
    print("near found")
else:
    print("didn't find")
