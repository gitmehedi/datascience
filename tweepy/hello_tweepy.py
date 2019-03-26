import json, os
import tweepy
import time, csv

ts = time.time()

CONSUMER_KEY = 'RWR5vlhSo9tLSHbtRN978VVSj'
CONSUMER_SECRET = '6HmLJCGlUMD482EKheTIn1q63VQxV3XHMzCYvsHsJx7s9Z8vok'
ACCESS_TOKEN = '236363487-MYKmhWdSewzPL89mUJVp1w70VKQIkqwKZXR1UE5K'
ACCESS_TOKEN_SECRET = 'eQBKYIL3rpu9hNP8pdhbQRYPeAnOdh3Eunez1bEjvHurf'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

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
