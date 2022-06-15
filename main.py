import os
import tweepy as tw
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import dotenv

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
#api = tw.API(auth, wait_on_rate_limit=True)
api = tw.Client(bearer_token=bearerToekn, consumer_key=consumerKey, consumer_secret=consumerSecret, access_token=accessToken, access_token_secret=accessSecret)

# Set up query for twitter data
hashtag = '#cryptocurrency'
query = tw.Cursor(api.search_recent_tweets, q=hashtag).items(100)
tweets = [{'Tweet': tweet.text, 'Timestamp': tweet.created_at} for tweet in query] 
print(tweets)

