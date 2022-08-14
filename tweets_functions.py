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

def top10_days_with_most_tweets(tweets):
    """
    Returns the top 10 days with the most tweets
    """
    date_tweet_count = dict()
    for tweet in tweets:
        date = tweet['date'][:10]
        if date in date_tweet_count:
            date_tweet_count[date] += 1
        else:
            date_tweet_count[date] = 1
    top10 = []
    # Get the top 10 days with the most tweets from the dictionary
    for key, value in sorted(date_tweet_count.items(), key=lambda item: item[1], reverse=True):
        if len(top10) == 10:
            break
        top10.append({'date': key, 'tweetCount': value})

    return top10

def top10_used_hashtags(tweets):
    """
    Returns the top 10 used hashtags
    """
    hashtag_dict = dict()
    for tweet in tweets:
        text = tweet['content']
        hashtags = [hashtag for hashtag in text.split() if hashtag.startswith('#')]
        if len(hashtags) > 0:
            for hashtag in hashtags:
                if hashtag in hashtag_dict:
                    hashtag_dict[hashtag] += 1
                else:
                    hashtag_dict[hashtag] = 1
    top10 = []
    # Get the top 10 hashtags from the dictionary
    for key, value in sorted(hashtag_dict.items(), key=lambda item: item[1], reverse=True):
        if len(top10) == 10:
            break
        top10.append({'hashtag': key, 'count': value})
    return top10