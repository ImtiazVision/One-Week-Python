tweet = input("Enter a tweet: ")
tweet_char_count = len(tweet)
max_tweet_chars = 140

if tweet_char_count > max_tweet_chars:
    print(f"Tweet is {tweet_char_count - max_tweet_chars} characters too long")
else:
  print(f"That {tweet_char_count} characters tweet is fine")