import data_handler

def main():
  tweets = data_handler.read_data('farmers-protest-tweets-2021-03-5.json')

  print(tweets[0])

if __name__ == '__main__':
  main()