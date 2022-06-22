import pandas as pd
import tweepy
from os import listdir
from os.path import isfile, join

consumer_key = 'CHo8OPU0WZBb17cd0FMt8H40n'
consumer_secret = 'qkizWofRqvsn7KYvZD5U1U16nAyeFKat96vRLNQE4sjDjTuNwg'
access_token = '1503040220572356614-I0a2jrr2etftLKFPRrOUfvwMapxl3x'
access_token_secret = 'JADc0N1lv54648JAkwd0jLSs44N92sT2VSlEHIYpswx6w'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
path = "./files/"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]


def fetch_tw(ids, name):
    tw_statuses = api.lookup_statuses(ids, tweet_mode="extended")
    data = pd.DataFrame()
    for count, status in enumerate(tw_statuses):
        tweet_elem = {"tweet_id": status.id,
                      "tweet": status.full_text,
                      "date": status.created_at,
                      "user": status.user.screen_name,
                      "tweet_url": urls[count]}
        data = data.append(tweet_elem, ignore_index=True)
    data.to_csv(f"tweets_{name}.csv", mode="a", sep=";")



for item in onlyfiles:
    tweet_url = pd.read_csv(f"./files/{item}", index_col=None, header=None, names=["tweet_urls"])
    tweet_url.head()
    urls = tweet_url['tweet_urls'].tolist()
    af = lambda x: x["tweet_urls"].split("/")[-1]
    tweet_url['tweet_id'] = tweet_url.apply(af, axis=1)
    ids = tweet_url['tweet_id'].tolist()
    total_count = len(ids)
    chunks = (total_count - 1) // 50 + 1
    name = item[15:-4]
    for i in range(chunks):
        lst = ids[i * 50:(i + 1) * 50]
        result = fetch_tw(lst,name)
