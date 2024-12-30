import tweepy

# Replace these with your own credentials
api_key = ""
api_secret = ""
access_token = ""
access_token_secret = ""

# Authenticate with Twitter
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# Test authentication
try:
    api.verify_credentials()
    print("Authentication successful!")
except tweepy.TweepError as e:
    print(f"Authentication failed: {e}")
