tweet = input("Enter a tweet: ")
tweet_char_count = len(tweet)

if tweet_char_count > 140:
    print(f"Tweet is {tweet_char_count - 140} characters too long")
else:
  print(f"That {tweet_char_count} characters tweet is fine")