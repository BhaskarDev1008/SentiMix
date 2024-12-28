import tweepy
import pandas as pd

# Replace with your Twitter API V2 Bearer Token
bearer_token = "AAAAAAAAAAAAAAAAAAAAACcmxwEAAAAAnK2s2VsdMOU%2B3uznFAi7ADbXOwo%3D5uAfJ9VK2riyUvAcCFKFfQAYAmWHnLt1ZlZqLbYEL8JXNFkBID"

# Authenticate using Tweepy with V2 (Bearer Token)
client = tweepy.Client(bearer_token=bearer_token)

# Define search query and parameters
search_query = "awesome OR बढ़िया OR बेकार -is:retweet lang:en"

# Collect tweets using the V2 API
response = client.search_recent_tweets(query=search_query, max_results=100)

# Store tweets data in a list
data = []
for tweet in response.data:
    data.append({
        "text": tweet.text,
        "created_at": tweet.created_at
    })

# Convert to DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("sentimix_tweets.csv", index=False)
print("Tweets collected and saved to sentimix_tweets.csv")
