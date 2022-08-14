import data_handler
import tweets_functions

def main():
  tweets = data_handler.read_data('farmers-protest-tweets-2021-03-5.json')

  top10 = tweets_functions.top10_retweeted(tweets)

if __name__ == '__main__':
  main()