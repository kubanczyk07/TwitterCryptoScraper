#get a list of twitter profiles
#get them into list in your program or follow all of them on twitter
#consider creating a twitter bot to automate following them
#iterate through profiles' tweets
#make sure a correct data form and search for your targets
#analyze data by different criterias
#save your results
from collections import UserString
from numpy import apply_over_axes, insert
from requests import Request, Session
import json
import pprint
from itertools import count
import tweepy, datetime, time
import pytz
import webbrowser
import configparser
import pandas as pd 
import pprint
from furas import coins_list

callbacks_uri = 'oob'

config = configparser.ConfigParser()
config.read('settings.ini')
consumer_key=config['Twitter']['consumer_key']
consumer_secret=config['Twitter']['consumer_secret']
access_token=config['Twitter']['access_token']
access_token_secret=config['Twitter']['access_token_secret']

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
print('udalo sie')
api = tweepy.API(auth)
# me = api.me()
# print(me.screen_name)

public_tweets = api.home_timeline(count=500)
tweets_content=['']
for tweet in public_tweets:
    author=tweet.author.name
    tweet=tweet.text
    tweets_content.append(tweet)
unified_content=''
unified_content=unified_content.join(tweets_content)

# print(unified_content)
# def crypto_counter(symbol, start=0):
#     lets_count=f'{symbol}={start}'
#     return start
# def insert_your_crypto_symbols():
#     input('what cryptos you want to search for:')
#     return input 
def big_counter():
    users=['AltcoinSherpa', 'ZssBecker', '321Crypto', 'Kamil Jarzombek', 'Phil Konieczny', 'JRNYcrypto', 'LadyofCrypto1', 'TiggersCrypto']
    all_tweets_list=[]
    count=0
    limit=10000
    print('111111111111111111111')
    for user in users:
        tweets=api.user_timeline(screen_name=user, count=limit, tweet_mode='exntended')
        for tweet in tweets:
            all_tweets_list.append(tweet.text)
            for i in all_tweets_list:
                print(i.items())
                if i in all_tweets_list:
                    count+=1
    print(count)
print(big_counter())





# columns=['User', 'Tweet']
# data = []
# for tweet in tweets:
#     # coinmarket_data = json.loads(tweet.text)
#     print(tweet.text)

# print(coins_list)

# if coinmarket_data:
#     for tweet in coinmarket_data:
#         print(tweet['name'])
#         print(tweet['date'])

# getting a list of coins I want to include in my calculations
# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/historical'
 
# parameters={
#     'start':'10',
#     'limit':'1000'
# }
# key=open('coinmarketcap_key.txt').read()
# headers={
#     'Accepts':'application/json',
#     'X-CMC_PRO_API_KEY':key,
# }

#print(type(dir(tweet)))
#for i in dir(tweet):
#print(i)
#print(dir(tweet)['author']) 