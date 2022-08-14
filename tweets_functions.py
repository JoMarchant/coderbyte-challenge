def top10_retweeted(tweets):
    """
    Returns the top 10 most retweeted tweets
    """
    top10 = []
    for tweet in tweets:
        max_retweeted = max(top10, key=lambda x: x['retweetCount']) if len(top10) > 0 else 0
        retweet_count = tweet['retweetCount']
        if len(top10) == 10:
            if retweet_count > max_retweeted['retweetCount']:
                top10.remove(min(top10, key=lambda x: x['retweetCount']))
                top10.append(tweet)
        else:
            top10.append(tweet)
    top10.sort(key=lambda x: x['retweetCount'], reverse=True)
    return top10

def top10_users_with_most_tweets(tweets):
    """
    Returns the top 10 users with the most tweets
    """
    top10 = []
    for tweet in tweets:
        max_tweeted = max(top10, key=lambda x: x['user']['statusesCount']) if len(top10) > 0 else 0
        retweet_count = tweet['user']['statusesCount']
        if len(top10) == 10:
            if retweet_count > max_tweeted['user']['statusesCount']:
                top10.remove(min(top10, key=lambda x: x['user']['statusesCount']))
                top10.append(tweet)
        else:
            top10.append(tweet)
    top10.sort(key=lambda x: x['user']['statusesCount'], reverse=True)
    return top10