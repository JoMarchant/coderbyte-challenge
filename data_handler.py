import json


def read_data(file_name):
    tweets = []
    with open(file_name) as f:
        for jsonObj in f:
            tweet = json.loads(jsonObj)
            tweets.append(tweet)

    return tweets
