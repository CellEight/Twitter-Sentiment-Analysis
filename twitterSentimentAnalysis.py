from twitter_keys import *
import tweepy, sys
from textblob import TextBlob

def main():
    #Verify search term is present
    try:
        search_term = sys.argv[1]
    except:
        print("Please call with search term.")
        return
    #Authorize twitter api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    #Get tweets that matched search term
    public_tweets = api.search(search_term)
    #Get tweet Sentiment and output
    for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)

if __name__ == "__main__":
    main()
