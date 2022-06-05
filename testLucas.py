from operator import contains
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters={
  'start':'1',
  'limit':'5',
  'convert':'USD'
}

key=open('coinmarketcap_key.txt').read()
headers={
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': key,
}

session = Session()
session.headers.update(headers)

try:
	response = session.get(url, params=parameters)
	coinmarket_data = json.loads(response.text)
except (ConnectionError, Timeout, TooManyRedirects) as e:
	print(e)

print(coinmarket_data)

coins=[]
if coinmarket_data:

	for d in coinmarket_data['data']:

		print(d['name'])
		coins.append(d['name'])
		print(d['circulating_supply'])
		print(d['platform'])
		print()
print(coins)
print(len(coins))
print(d.items())

# Zamień listę słowników w df
df = pd.DataFrame(coinmarket_data['data'])
#print(df)

# Zapisz df jako csv
df.to_csv('coinmarket_test.csv')

# Remapping
mapa = {"ync8ndcm3bc" : 'KubaCoin', "ouvsa4tlnwh" : 'O', "1gwa8hqe81f": 'V', "3qhqp71ka4s" : 'E', "8wvvoz7743v": ':)'}
df2=df.replace({"name": mapa})

print(df2)