import data_handler
import tweets_functions


def main():
    # tweets = data_handler.read_data('farmers-protest-tweets-2021-03-5.json')
    tweets = data_handler.read_data_limited('farmers-protest-tweets-2021-03-5.json', 100)

    top10_retweeted = tweets_functions.top10_retweeted(tweets)
    top10_users_with_most_tweets = tweets_functions.top10_users_with_most_tweets(tweets)



if __name__ == '__main__':
    main()
