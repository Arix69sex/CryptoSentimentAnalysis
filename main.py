import os
from xml.etree.ElementTree import tostring
import tweepy as tw
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import dotenv
import nltk
from nltk.corpus import stopwords
from textblob import Word, TextBlob

# nltk.download() 
# nltk.download('stopwords')
# nltk.download('wordnet')
tweets = ''
# Setting enviroment variables
dotenv.load_dotenv(dotenv.find_dotenv())
bearerToekn = os.getenv("BEARER_TOKEN")
consumerKey = os.getenv("API_KEY")
consumerSecret =  os.getenv("API_SECRET")
accessToken = os.getenv("ACCESS_TOKEN")
accessSecret =  os.getenv("ACCESS_TOKEN_SECRET")

# Authentification
auth = tw.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken,accessSecret)
api = tw.API(auth, wait_on_rate_limit=False)
#api = tw.Client(bearer_token=bearerToekn, consumer_key=consumerKey, consumer_secret=consumerSecret, access_token=accessToken, access_token_secret=accessSecret)

def get_tweets(hashtag, quantity):
    # Set up query for twitter data
    query = tw.Cursor(api.search_tweets, q=hashtag).items(quantity)
    return [{'Tweet': tweet.text, 'Timestamp': tweet.created_at} for tweet in query] 

# Putting tweets inton dataframe so its more readable
#df = pd.DataFrame.from_dict(get_tweets('#bitcoin'))
#print(df.head())
hashtag = '#bitcoin'
def preprocess_tweets(tweet, custom_stopwords, stop_words):
    processed_tweet = tweet
    processed_tweet.replace('[^\w\s]', '')
    processed_tweet = " ".join(word for word in processed_tweet.split() if word not in stop_words)
    processed_tweet = " ".join(word for word in processed_tweet.split() if word not in custom_stopwords)
    processed_tweet = " ".join(Word(word).lemmatize() for word in processed_tweet.split())
    return(processed_tweet)

def process_sentiment(value):
    print(value)
    if value > 0:
        return str(abs(round(value * 100, 2))) + '% - ' + "Bullish market"
    elif value < 0:
        return str(abs(round(value * 100, 2))) + '% - ' +  "Bearish market"
    else:
        return"Neutral market"

def make_decision(value):
    print("do something")

def main(quantity):
    df = pd.DataFrame.from_dict(get_tweets(hashtag, quantity))
    stop_words = stopwords.words('english')
    custom_stopwords = ['RT', hashtag]

    df['Processed Tweet'] = df['Tweet'].apply(lambda x: preprocess_tweets(x, custom_stopwords, stop_words))
    df.head()

    df['polarity'] = df['Processed Tweet'].apply(lambda x: TextBlob(x).sentiment[0])
    df['subjectivity'] = df['Processed Tweet'].apply(lambda x: TextBlob(x).sentiment[1])
    print(df.query('subjectivity != 0'))
    polarity_value = df.query('subjectivity != 0')["polarity"].mean()
    return process_sentiment(polarity_value), df.query('subjectivity != 0')