import json, os
import tweepy
import time, csv
from config import config

ts = time.time()

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
data = []
public_tweets = api.home_timeline()

file_json = 'data-' + str(int(ts)) + '.txt'
file_csv = 'data' + str(int(ts)) + '.csv'

with open(os.path.join('/opt/datascience/tweepy/data', file_csv), 'w') as file_csv:
    data = csv.DictWriter(file_csv, ['id', 'tweet', 'datetime'])
    data.writeheader()
    for tweet in public_tweets:
        data.writerow({'id': tweet.id, 'tweet': tweet.text.encode('utf-8'), 'datetime': str(tweet.created_at)})
