import json


def read_data(file_name):
    tweets = []
    with open(file_name) as f:
        for jsonObj in f:
            tweet = json.loads(jsonObj)
            tweets.append(tweet)

    return tweets

def read_data_limited(file_name, limit):
    tweets = []
    with open(file_name) as f:
        for jsonObj in f:
            tweet = json.loads(jsonObj)
            tweets.append(tweet)
            if len(tweets) == limit:
                break

    return tweets
