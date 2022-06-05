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

limit=400
tweets=api.user_timeline(screen_name='ZssBecker', count=limit, tweet_mode='exntended')
for tweet in tweets:
    tweet=tweet.text
    if 'DXY' in tweet:
        print(tweet)