from requests import Request, Session
import json
import tweepy, datetime, time
import pytz
import webbrowser
import configparser
import pandas as pd 
from furas import coin_name, coin_symbol, coin_dictionary
from collections import Counter 

callbacks_uri = 'oob'

config = configparser.ConfigParser()
# print('xxxx', dir(config))
# time.sleep(10)
config.read('settings.ini')
consumer_key=config['Twitter']['consumer_key']
consumer_secret=config['Twitter']['consumer_secret']
access_token=config['Twitter']['access_token']
access_token_secret=config['Twitter']['access_token_secret']

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
print('udalo sie')
api = tweepy.API(auth)

# Our parameters
first_counter=0
second_counter=0
users=['AltcoinSherpa', 'ZssBecker', '321Crypto', 'Kamil Jarzombek', 'Phil Konieczny', 'JRNYcrypto', 'LadyofCrypto1', 'CoinTrendz']
all_tweets_list=[]
limit=10000
# polarity=0
firstcoin='Avalanche' #input('insert FULL name of a cryptoccurency you want to search for:')
secondcoin='NEAR Protocol' #('insert FULL name of the second cryptoccurency you want to search for:')
# here we list most possible ways people can call a particular cryptocurrenc
coin_reprezentation=[]
coins_list_counter=0

def check_your_coin_name(coin):
    if coin in coin_dictionary:
        print('Congrats, you inserted a correct full name of your cryptocurrency')
    else:
        print('insert a correct, full name of your coin. when in doubt check coinmarketcap.com')

def coin_symbols_maker(coin):
    coin_reprezentation = []
    coin_reprezentation.append(coin.lower())
    coin_reprezentation.append(coin.upper())
    coin_reprezentation.append(coin.capitalize())
    for key in coin_dictionary.keys():
        if coin==key:
            print(key, coin)
            coin_reprezentation.append(coin_dictionary[key])
            coin_reprezentation.append(coin_dictionary[key].lower())
            coin_reprezentation.append(coin_dictionary[key].capitalize())
    return coin_reprezentation

print('NOW CHECK if results show symbols of the coin you are looking for...')   
first_coin=coin_symbols_maker(firstcoin)
print(first_coin)
second_coin=coin_symbols_maker(secondcoin)
print(second_coin)
time.sleep(5)
# import sys
# sys.exit(0)
# I want to convert full crypto names into abbreviations and vice versa. 
# For that I need to create a dictionary and scrape Coinmarketcap to get couples

print('111111111111111111111')
# def scrapping_from_profiles():
first_counter=0
second_counter=0
for user in users:
    tweets=api.user_timeline(screen_name=user, count=limit)
    # print('CHECKING tweets methods', dir(tweets))
    # print('checking ids methods', dir(tweets.ids))
    # time.sleep(30)
    for tweet in tweets:
        tweet=tweet.text
        tweet=tweet.replace('RT', '')
        if tweet.startswith(' @'):
            position=tweet.index(':')
            tweet=tweet[position+2:]
        if tweet.startswith('@'):
            position=tweet.index(' ')
            tweet=tweet[position+2:]
        all_tweets_list.append(tweet)
    for tweet in all_tweets_list:
        for s in first_coin:
            if s in tweet:
                # print('1', tweet)
                first_counter+=1
        for sy in second_coin:
            if sy in tweet:
                second_counter+=1
                # print('2', tweet)
                # print()
    # return scrapping_from_profiles

# print(all_tweets_list)
print(first_counter)
print(second_counter) 

if first_counter > second_counter:
    print("Coin no.1 was mentioned more times than the 2nd coin")
elif second_counter > first_counter:
    print("Coin no.1 was mentioned more times than the 2nd coin")
elif first_counter == second_counter:
    print("Both coins were mentioned the same amount of times")
else:
    print("Wow, your altcoin was more popular on Twitter than Bitcoin")

all_tweets_count=[]
print('Coin that was mentioned the most amount of times is:')
for tweet in all_tweets_list:
        for coinsymbol in coin_dictionary:
            if coinsymbol in tweet:
                all_tweets_count.append(coinsymbol)
        the_most_common = Counter(all_tweets_count)
print('The most common coins are:', the_most_common)

       

# I want to ad a functionality that scrapes comments from given profiles
# existing=0
# print(dir(all_tweets_list))
# for key in all_tweets_list:
#     if 'avax' in key:
#         existing+=1
#     else:
#         pass
# print(existing)