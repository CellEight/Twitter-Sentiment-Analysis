from twitter_keys import *
import tweepy, sys, csv
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
    tweet_lib = []
    for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        tweet_dict = {'Author': tweet.author.name, 'Date': tweet.created_at, 'Text': tweet.text, 'Sentiment': analysis.sentiment}
        tweet_lib.append(tweet_dict)
        #print(dir(tweet.author))
    with open(search_term+".csv", 'w') as csvfile:
        field_names = ['Author', 'Date', 'Text', 'Sentiment']
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        for row in tweet_lib:
            writer.writerow(row)
if __name__ == "__main__":
    main()
